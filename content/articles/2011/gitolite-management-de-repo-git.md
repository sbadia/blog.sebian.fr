Title: Gitolite, management de repo git
Date: 2011-04-29 01:18
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: debian, git, gitolite
Slug: gitolite-management-de-repo-git
Modified: 2014-02-23 17:07

Je voulais tester [gitorious](http://gitorious.org/) mais j'ai été un peu découragé par le nombre des dépendances... Je me suis donc installé, un gitolite + gitweb et redmine, et c'est parfait !

## Apéro

Au niveau des pré-requis, il ne faut pas grand chose, juste un accès ssh, web, et un peu d'espace disque, pour que ce soit le plus propre possible, on crée au préalable deux utilisateurs.

Git qui sera l'utilisateur lambda

    :::console
    adduser --system --shell /bin/bash --gecos 'gitolite admin' --group --home /home/gitadmin gitadmin

Gitadmin, comme son nom l'indique l'admin pour gitolite.

    :::console
    adduser --system --shell /bin/bash --gecos 'gitolite user' --group --home /home/git git

On install git

    :::console
    apt-get update && apt-get install git-core ssh

Et on commence par autoriser gitadmin à se connecter en git sur la machine

    :::console
    su - gitadmin
    ssh-keygen -t dsa

En copiant la clée publique dans le *authorized\_keys* de git.

    :::console
    cat .ssh/id_dsa.pub >> /home/git/.ssh/authorized_keys

## Plat

Disponible sur [github gitolite](http://github.com/sitaramc/gitolite/) se présente sous forme d'un repo.
**Voir aussi la méthode apt... en base de l'article**

    :::console
    git clone git://github.com/sitaramc/gitolite.git
    cd gitolite
    src/gl-easy-install git localhost gitadmin

On reponds à deux trois questions, et l'installateur nous génère un dépôt gitolite-admin. Dans ce dernier, nous retrouvons deux repertoires, *keydir*, où sont stockés les clées publiques des utilisateurs, et *conf* où est stocké la conf des repos et les droits.

Gitolite-admin est lui-même un repo, et c'est le push de ce repo qui provoque, la création/mise a jours des droits, repo concernés…

## Dessert

Pour la configuration coté client on peux commencer par configurer un host dans notre *~/.ssh/config*

    :::console
    Host gitbian
      Hostname sebian.fr
      User git
      Port 666
      IdentityFile /home/%u/.ssh/id_dsa

On se connecte ensuite afin de voir nos repository et nos droits.  

    :::console
    ssh gitldn

Ce qui provoque un output dans le genre.

    :::console
    hello sbadia, the gitolite version here is v2.0-27-gd74e58b
    the gitolite config gives you the following access:
      R   W   ldn
     @R_ @W_  testing
    Connection to sebian.fr closed.

Nous pouvons alors essayer de cloner le repo ldn

    :::console
    git clone gitbian:ldn.git

## Bonus

Alertes jabber au moment d'un commit :)

    :::console
    # file repo.git/hooks/post-recieve
    git log -1 | sendxmpp -t -s "*** repo.git/refs/heads/master - `date` ***" sebian seb@sebian.fr

Et voila :)

[EDIT] Je n'avais pas vu, mais un paquet debian gitolite est aussi disponible, c'est donc encore plus simple.

    :::console
    apt-get install gitolite
    dpkg-reconfigure gitolite

Et on remplace *gitolite* par *git* pour coller avec notre install, et */var/lib/gitolite* par */home/git*, on colle la clé de gitadmin et voila le tour est joué.
