Title: Wmii, la productivité assurée
Date: 2010-02-14 14:19
Author: Sebastien
About_author: ASRALL Student
Category: Tips
Tags: Debian, Tips, Wmii
Slug: wmii-la-productivite-assuree
Modified: 2014-02-23 17:07

## Intro

Depuis le début de l'année d'Asrall j'utilise Wmii, pour ceux qui ne connaissent pas, c'est un Windows Manager pour Linux. Je ne peux vraiment plus m'en passer, niveau productivité c'est le top, les fenêtres sont redimensionnés à la création pour occuper le plus de place.

Optimisation de l'espace disponible, navigation tout au clavier, gestion de bureau virtuels...

## Installation

Aller je vous fait un petit tuto de mon installation type d'une debian

### Debian

On commence par installer debian (ah bon???) oui oui !!

    :::console
    apt-get install sudo xserver gdm`

Sudo car c'est bien pratique, ne pas oublier de se rajouter dans les sudoers, avec un visudo en root !

Xserver (xserver-xorg) pour la fenêtre graphique, et le gdm pour un connexion simplifié (oui à force c'est pénible le startx), gdm permet aussi de "switcher" entre plusieurs sessions graphiques.

    :::console
    apt-get remove --purge vim-tiny && apt-get install vim`

Oui, j'aime vraiment pas vim-tiny, vim (le vrai) c'est mieux.

    :::console
    apt-get install build-essential thunar nitrogen iceweasel

Build-essential, pour le gcc, et les paquets indispensables pour compiler du code...

Thunar qui est un excellent gestionnaire de fichiers, issu de xfce; Nitrogen pour la gestion de wallpaper et iceweasel, le navigateur ;)

Pour Nitrogen il suffit de tapper dans un terminal

    :::console
    nitrogen Dossier-Images
    apt-get install rxvt-unicode

Un terminal qui gère la transparence...

## Optimisations

Pour prompt en couleurs, renommez le en .bashrc dans votre home.

Vim en couleur, avec les num, renommez le en .vimrc dans votre home.

### Wmii

Passons aux choses serieuses

    :::console
    apt-get install wmii`

Ahah oui je vous entends d'ici, oui oui c'est tout ! ce magnifique gestionnaire de fenêtres tient en 2mo il me semble et environ 1000 lignes de code, comme l'autre dirais, ce n'est pas la taille qui compte :p

### Optimisations

Style terminal, (transparence, et modif police, renommez le en .Xdefaults
Un wmiirc, à modifier bien sur ;), à placer dans un dossier .wmii dans votre home.

## Utilisation

Il y a un très bon tuto sur les docs d'Ubuntu-fr, je ne détaillerais donc pas trop ;), juste l'essentiel...

* alt + p Liste des programmes ( il suffit d'écrire et les programmes défilent dans la barre de statut)
* alt + entrée Ouverture d'un terminal.
* alt + a liste des actions (menu spécial de gestion de wmii)
* alt + [H/J/K/L] Sélectionner la fenêtre de [gauche / bas / haut / droite]
* alt + Shift + [H/J/K/L] Déplacer la fenêtre à [gauche / bas / haut / droite]
* alt + n Ouverture d'un bureau virtuel (une vue en réalité) dont n est le chiffre allant de 0 à 9
* alt + shift + n Envoie la fenêtre courante vers le bureau n dont n est le chiffre allant de 0 à 9
* alt + Shift + C Fermeture de la fenêtre active.
* alt + d Les fenêtres se partagent l'espace vertical (d = défaut)
* alt + espace Passe de la vue normale en vue flottante et vice-versa
* alt + shift + espace Passe la fenêtre courante de la vue classique à la vue flottante et vice-versa
