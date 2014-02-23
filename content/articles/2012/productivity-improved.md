Title: Productivity improved
Date: 2012-12-21 01:05
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: awesome, pentadactyl, powerline, prezto, tabbedex, tomorrow, urxvt, vim, vundle
Slug: productivity-improved
Modified: 2014-02-23 17:07

Aller ça faisait un moment que je souhaiter poster ceci, avec l'avènement des repos [dotfiles](http://dotfiles.github.com/) sur Github c'est encore plus vrai…

Voici donc juste un petit post, pour vous narrer mon environnement de bureau dans ses moindre détails et ses petites suxeries de configs.

## Environnent de bureau

J'utilise [awesome](http://awesome.naquadah.org/) (tilling manager, configuration en lua, extensible à souhait), coté suxeries, j'utilise [eminent](http://awesome.naquadah.org/wiki/Eminent), ce plugin permet d'allouer/créer dynamiquement les tags (comprendre bureaux), ma config est odieusement copié sur celle de [Thomas](https://github.com/Schnouki/dotfiles/tree/master/awesome) !

## Terminal

URxvt, simple rapide efficace, configurable à souhait depuis le fichier *~/.Xdefaults*.

URxvt permet d'inclure des modules externes asses facilement, j'utilise d'ailleurs [tabbedex](https://github.com/stepb/urxvt-tabbedex) (un tabbed amélioré) dispo ici.

Coté thème, je suis en ce moment sur [tomorrow](https://github.com/chriskempson/tomorrow-theme), après être passé par [solarized](http://ethanschoonover.com/solarized).

## Shell

Zsh bien sûr ! Mais pas «stock» à la grand papa ;-) Je suis resté longtemps sur [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh), mais j'ai finalement succombé à un fork, [prezto](https://github.com/sorin-ionescu/prezto), je préfère la philosophie, et la configuration…

## Éditeur

Vi, je ne lance pas de troll éditeur, bien que ce billet soit publié un trolldi…

Pour la gestion des plugins après être passé des vimball (méthode grand papa), aux git submodules (pas super gérable dans le temps), j'ai découvert [Vundle](https://github.com/gmarik/vundle), et là c'est le top ! (très similaire à bundle).

Coté plugins je vous conseille NerdTree, Powerline, Syntastic, … Mon [vimrc](https://github.com/sbadia/grimvim/blob/master/vimrc) est dispo sur github.

## Navigateur

Un bon vieux firefox (iceweasel), mais avec quelques plugins, à commencer par [pentadactyl](http://5digits.org/pentadactyl/) et TabMix Plus (sans oublier les essentiels Ghostery,Adblock,NoScript,WebDeveloper, et j'en passe.)

*git.sebian.fr:suxeries.git*
