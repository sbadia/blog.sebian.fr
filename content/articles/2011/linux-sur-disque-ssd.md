Title: Linux sur disque SSD
Date: 2011-10-09 22:13
Author: Sebastien
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: debian, linux, SSD
Slug: linux-sur-disque-ssd
Modified: 2014-02-23 17:07

Il y a quelque mois, j'ai eu un petit soucis de contrôleur mémoire sur mon SSD, heureusement la panne est passé sous garantie, mais depuis, je n'ai pas pris le temps de réinstaller, c'est chose faite maintenant, bon ok j’arrête de raconter ma vie ;)

## Installation

Depuis la version 2.2 de parted, il réalise automatiquement un alignement sur 2048 secteur, ce qui correspond donc bien pour notre SSD (alignement des blocs).

Coté système de fichier j'ai choisi du ext4 pour les optimisation TRIM, et pour bénéficier de la journalisation quand même…

    :::console
    mkfs.ext4 -b 4096 -E stride=32 /dev/sda1

## Optimisations

Ayant une machine avec 4Go de ram, j'ai désactivé le swap, d'une part, et j'ai placé quelque points de montage en ramfs, notamment un tmpfs,

    :::console
    none /tmp tmpfs defaults,nosuid,nodev,noexec 0 0

Ou pour les utilisateurs de iceweasel/firefox, le .mozilla

    :::console
    none /home/sbadia/.mozilla tmpfs defaults,uid=1000,gid=1000,mode=750     0 0

L'inconvénient c'est que les données sont perdues au démarrage (vu qu'elle sont dans la ram...), il suffit donc de synchroniser avec un autre répertoire au boot, et à l'extinction ;)

    :::bash
    #!/bin/sh
    ### BEGIN INIT INFO
    # Provides: Mozilla sbadia profile in a ramfs
    # Required-Start: $local_fs $syslog $remote_fs
    # Required-Stop: $local_fs $syslog $remote_fs
    # Default-Start: 2 3 4 5
    # Default-Stop: 0 1 6
    # Short-Description: Sbadia .morilla ramfs
    # Description: Backup or Restore sbadia mozilla in a ramfs
    ### END INIT INFO
    REF=/home/sbadia/.mozilla_ref/
    DIR=/home/sbadia/.mozilla/
    case "$1" in
      start)
        echo -n "Moz-ramfs: extract mozzila user profile..."
        [ ! -d $DIR ] && mkdir -p $DIR
        rsync -a $REF $DIR
        echo "[OK]"
        ;;
      stop)
        echo -n "Moz-ramfs: backup mozilla user profile..."
        rsync -a $DIR $REF
        echo "[OK]"
        ;;
      *)
        echo "Usage: $0 {start|stop}"
        exit 1
        ;;
    esac

et de mettre à jour les scripts d'init

    :::console
    update-rc.d moz-ramfs defaults

## Options de montage

Une autre optimisation est d'ajouter l'option "noatime" à nos points de montage, cette option permet de ne pas mettre à jour les horodatages d'accès aux inœuds sur le système de fichiers.

    :::console
    /dev/sda1  /               ext4    errors=remount-ro,noatime 0       1

Et si noyau superieur à 2.6.33 et installation en ext4, on peux activer le trim automatique, avec l'option "discard".

    :::console
    /dev/sda1  /               ext4    errors=remount-ro,noatime,discard 0       1

Une autre idée est de désactiver le logging…

Pour plus d'infos lisez le Tuto de [Forum Hardware](http://forum.hardware.fr/hfr/OSAlternatifs/Hardware-2/recensement-optimisation-conseils-sujet_69473_1.htm), il est de très bonne qualité !

## Sources

* [Wikipedia SSD](http://fr.wikipedia.org/wiki/Solid-state_drive)
* [ForumHardware SSD](http://forum.hardware.fr/hfr/OSAlternatifs/Hardware-2/recensement-optimisation-conseils-sujet_69473_1.htm)
