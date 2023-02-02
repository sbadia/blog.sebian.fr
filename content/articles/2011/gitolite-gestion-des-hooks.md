Title: Gitolite gestion des hooks
Date: 2011-10-29 17:32
Author: Sebastien
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: git, gitolite, hooks
Slug: gitolite-gestion-des-hooks
Modified: 2014-02-23 17:07

Je suis passé depuis un petit moment à [Gitolite](https://github.com/sitaramc/gitolite) pour la gestion de mes repos git (aussi bien pour le boulot, que perso), je détailler aujourd'hui, un atout pas négligeable qui est la gestion centralisé des hooks.

Je suppose que vous avez fait votre install avec le paquet (ici [Debian](http://debian.org)), et donc que gitolite est installé dans */var/lib/gitolite*.

On commence donc par créer un hook */var/lib/gitolite/.gitolite/hooks/common/post-receive* qui sera donc commun à tous les nouveaux repo crées.

    :::bash
    #!/bin/sh
    # sbadia
    while read oldrev newrev refname do
      echo $oldrev $newrev $refname | . /usr/share/doc/git-core/contrib/hooks/post-receive-email
      for i in $(git config xmpp.jabbernotif);do git log $oldrev..$newrev $refname | sendxmpp -t $i;done
    one

Et on oublie pas de le rendre exécutable.

Il faut ensuite activer la modification dynamique de configuration, pour ça si vous ne souhaitez pas vous embêter, il suffit de mettre un ".\*"

    :::shell-session
    sed -e 's/^\$GL_GITCONFIG_KEYS\ =\ "";/#$GL_GITCONFIG_KEYS\ =\ "";/' \
      -e 's/^#\$GL_GITCONFIG_KEYS\ =\ "\.\*";/$GL_GITCONFIG_KEYS\ =\ ".*";/' \
      -i /var/lib/gitolite/.gitolite.rc

Afin d'éviter de créer des fichier *description* dans chaque repo, on peux maintenant utiliser les fonctions de création de conf dynamique. Je modifie donc le script d'envoi d'email du paquet git-core */usr/share/doc/git-core/contrib/hooks/post-receive-email*


    :::shell-session
    sed -e 's/^projectdesc=.*/projectdesc=$(git config repo.description)/' -i /usr/share/doc/git-core/contrib/hooks/post-receive-email

Tout ceci fait, on peux modifier la config de nos repos pour utiliser ces nouvelles [siouxeries](http://bleuchtang.fr/).

Dans la config gitolite coté client *gitolite-admin/conf/gitolite.conf*

    :::console
    @lestrois = riri fifi loulou
    # Super projet top secret
    repo projetsecret
      RW+ =   @lestrois
      R   =   donald
      config hooks.mailinglist = riri@duck.corp,fifi@duck.corp,loulou@duck.corp
      config hooks.envelopesender = gitolite@git.fr
      config hooks.emailprefix = "[projetsecret] "
      config hooks.showrev = "git show -C %s; echo"
      config repo.description = "Super projet git secret"
      config xmpp.jabbernotif = riri@jabber.duck.corp fifi@jabber.duck.corp loulou@jabber.duck.corp

Et voila, riri fifi et loulou seront notifié par mail et par jabber à chaque commit sur le projet "projetsecret" ;)

Le lien symbolique du hook post-recieve n'est crée que pour les nouveaux repo, il doit y avoir un moyen de rejouer la conf gitolite, mais je n'ai pas cherché ;)

    :::bash
    for i in $(ls /var/lib/gitolite/repositories/);
    do
      ln -sv /var/lib/gitolite/.gitolite/hooks/common/post-receive /var/lib/gitolite/repositories/$i/hooks/post-receive;
    done

[Documentation gitolite (repo spécifique)](https://github.com/sitaramc/gitolite/blob/pu/doc/gitolite.conf.mkd#_repo_specific_git_config_commands)
