Title: Tips GIT: nom de la remote par défaut différent de « master »
Date: 2016-04-02 12:01
Author: Sebastien Badia
About_author: Engineer @RedHat.
Category: Asrall
Tags: git, remote, master, tips
Slug: git-remote-master

Une petite astuce en mode mémo pour changer la branch par défaut d'un repo
GIT, assez pratique lorsqu'on utilise gitflow.

# Via l'option set-upstream-to (Git >= 1.8.0) en local

Pour changer les informations de suivi de sa branch local vis-à-vis de
l'upstream (disponible depuis git 1.8.0).

    :::bash
    ❯ git branch --set-upstream-to origin/develop

# Changement aussi du coté upstream

Il faut aussi changer l'HEAD sur le repo GIT remote, les commandes suivante
fonctionnent dans mon cas.

    :::bash
    ❯ git symbolic-ref HEAD refs/heads/develop
    ❯ git update-server-info

Coté client on vérifie:

    :::bash
    ❯ git remote show origin
    * remote origin
      Fetch URL: git.debian.org:/git/collab-maint/taskd.git
      Push  URL: git.debian.org:/git/collab-maint/taskd.git
      HEAD branch: develop
      Remote branches:
        develop      tracked
        pristine-tar tracked
        upstream     tracked
      Local branch configured for 'git pull':
        develop merges with remote develop
      Local ref configured for 'git push':
        develop pushes to develop (up to date)

La HEAD branch est bien develop, c'est tout ok :-)
