Title: Productivity improved2
Date: 2012-12-24 02:50
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: git, mutt, orgmode, repup, taskwarrior, TODO, vim
Slug: productivity-improved2
Modified: 2014-02-23 17:07


## Gestionnaires de tâches

Ne trouvant rien d'exceptionnel à [Org-Mode](http://www.vim.org/scripts/script.php?script_id=3642) pour la gestion des TODO (ou alors il faut que qqun me montre…), je me suis mis à [task warrior](http://taskwarrior.org/) (merci Pascal), vraiment super pratique, avec pleins de fonctionnalités, et avec l'auto-complétion de zsh, c'est top !

Récemment je suis tombé sur un [frontend web à task warrior](https://github.com/theunraveler/taskwarrior-web), encore un peu jeune, mais sympa.

## Gestion de repos

Avant c'était tout dans un répertoire *~/dev/* mais c'était avant :-)

J'utilise [mr](http://joeyh.name/blog/entry/introducing_mr/) (multi repository) pour le bootstrap, et je classe par url (*~/dev/github.com/sbadia/repo*, *~/dev/git.sebian.fr/repo*, …), c'est plus simple (merci Pascal). Mais comme mr fait du séquentiel (nottament pour le pull/update des repos), je me suis fait un petit script ruby, [repup](https://github.com/sbadia/grimtools/tree/master/repup), il gère mercurial, git et svn, il utilise peach (130 repos en 15sec…).

[EDIT] Avec mr il suffit d'augmenter le nombre de jobs (merci Lucas)

    :::console
    mr update -j 10

## Prise de notes

De ce coté, je n'ai pas encore **LA** solution, mais je part plutôt vers du [Org-Mode](http://www.vim.org/scripts/script.php?script_id=3642)

## Mails

Mutt bien sûr ! Mutt-patched, avec Offlineimap pour la récupération des mails et msmtp pour l'envoi, ma config est allègrement pompé sur celle
de [Tim Sharpe](https://github.com/rodjek/dotfiles/tree/master/.mutt)

Surtout n'hésitez pas si vous avec des logiciels bien sympa à faire
partager :-)
