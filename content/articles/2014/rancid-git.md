Title: Rancid GIT et scripts custom
Date: 2014-08-30 10:05
Author: Sebastien
About_author: Engineer @eNovance, Puppet addict and Net Neutrality defender.
Category: Asrall
Tags: Rancid, GIT, Custom, Expect, TCL
Slug: rancid-git

Dans le cadre de [Gitoyen](http://gitoyen.net/) (Opérateur réseau associatif), nous avions besoin de sauvegarder et suivre les changements de configuration de nos équipements.

# Intro rancid

Rancid, pour « Really Awesome New Cisco confIg Differ » (rien que ça :p) est un outil de backup/versionning destiné tout particulièrement aux équipements réseaux. Voir le site web de rancid [http://www.shrubbery.net/rancid/](http://www.shrubbery.net/rancid/).

## Rancid GIT

Rancid est disponible officiellement avec CSV/SVN comme backend CVS, comme ces outils sont un peu vieillissants (CVS de grand papa…), il existe un fork supportant GIT comme backend.

Les sources sont disponible sur GitHub, voir [rancid-git](https://github.com/dotwaffle/rancid-git).

Pour construire les paquets (Debian dans notre cas), il est possible d'utiliser [sbuild](https://wiki.debian.org/sbuild).

    :::bash
    mkdir foo;sudo sbuild-createchroot --make-sbuild-tarball=/var/lib/sbuild/wheezy-amd64.tar.gz wheezy foo http://ftp.fr.debian.org/debian
    git clone https://github.com/dotwaffle/rancid-git;cd rancid-git
    sbuild -A -d wheezy

## Configuration

Concernant la configuration de rancid lui même, je ne vais pas détailler ici, il suffit de lire le fichier d'install, ou de savoir utiliser un moteur de recherche :-)

Cet article est d'ailleurs bien fait : [network-backup-with-rancid](http://gohgarry.wordpress.com/2012/05/30/network-backup-with-rancid/)

*Note*: Dans notre cas il suffit de changer le nom du backend en : git

### Tips

Rancid crée un fichier de log à chaque run, et il ne nettoie pas… Il peut donc être nécessaire d'ajouter une tâche cron…

## Scripts custom

Par défaut rancid support un bon nombre d'équipements réseaux (voir [rancid-fe](https://github.com/dotwaffle/rancid-git/blob/8238d57b0931a4b161725c1f25edbe0df20834fa/bin/rancid-fe.in#L53-L92)), mais il utilise toujours de script expect pour parser le retour.

Mais avec des équipements exotiques, ou des routeurs linux (bird par exemple) il peut être nécessaire de se passer d'expect et de directement récupérer la config sur le flux de sortie d'une commande SSH.

C'est tout à fait possible moyennant quelques patchs.

Je « fork » le script zrancid (dans mon cas c'est un routeur linux quagga), et nous allons donc le modifier.

Au lieu d'utiliser zlogin (qui est le script expect pour les routeurs zebra, on va donc utiliser notre wrapper ssh).

    :::perl
    if ($file) {
        print STDERR "opening file $host\n" if ($debug);
        print STDOUT "opening file $host\n" if ($log);
        open(INPUT,"<$host") || die "open failed for $host: $!\n";
    } else {
        print STDERR "executing rancid-gitoyen -t $timeo -c\"$cisco_cmds\" $host\n" if ($debug);
        print STDOUT "executing rancid-gitoyen -t $timeo -c\"$cisco_cmds\" $host\n" if ($log);
        if (defined($ENV{NOPIPE}) && $ENV{NOPIPE} =~ /^YES/i) {
            system "rancid-gitoyen $host </dev/null > $host.raw 2>&1" || die "rancid-gitoyen failed for $host: $!\n";
            open(INPUT, "< $host.raw") || die "rancid-gitoyen failed for $host: $!\n";
        } else {
            open(INPUT,"rancid-gitoyen $host </dev/null |") || die "rancid-gitoyen failed for $host: $!\n";
        }
    }

Et voici donc le wrapper:

    :::bash
    #!/bin/sh
    key='/var/lib/rancid/.ssh/id_rsa'
    opts='-oBatchMode=yes -oCheckHostIP=no -oHashKnownHosts=no -oStrictHostKeyChecking=no -oPreferredAuthentications=publickey -oChallengeResponseAuthentication=no -oKbdInteractiveDevices=no -oConnectTimeout=3 -oUserKnownHostsFile=/dev/null -o LogLevel=quiet'
    user='blah'
    if [[ -z $1 ]]; then
      echo unknow host
      exit 1
    fi
    echo "$1# show version"
    ssh $opts -i $key -l $user $1 'show version'
    echo "$1# write term"
    ssh $opts -i $key -l $user $1 'write term'
    echo "$1# exit"

Pour lier le tout, il nous suffit maintenant d'ajouter notre nouveau type/script dans la [vendortable](https://github.com/dotwaffle/rancid-git/blob/8238d57b0931a4b161725c1f25edbe0df20834fa/bin/rancid-fe.in#L53-L92).

Et de déclarer notre équipement avec ce type.

    :::bash
    # router.db
    g4.par.gitoyen.net:gitoyen:up

Et voila =)
