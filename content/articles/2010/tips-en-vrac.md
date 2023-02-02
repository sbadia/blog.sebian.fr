Title: Tips en vrac...
Date: 2010-05-10 22:04
Author: Sebastien
About_author: ASRALL Student
Category: Tips
Tags: Debian, Tips
Slug: tips-en-vrac
Modified: 2014-02-23 17:07

Un petit article, plutôt sous forme de pense bête qu'autre chose...

## Date dans le bash\_history

Le fichier .bash\_history, contient les commandes tapés dans le terminal, mais il n'est pas daté, pour rajouter ça, rien de plus simple !

Editez votre */etc/bashrc* pour y rajouter ceci...

    :::console
    export HISTTIMEFORMAT="%h/%d - %H:%M:%S "

## Sed ou la puissance...

Une connexion ssh, et votre terminal, vous retourne que le fingerprint à changer, oui vous êtes au courant, puisque vous venez de réinstaller votre serveur...

Pour effacer la ligne 29 du fichier *known\_hosts*

    :::console
    sed -i .ssh/known_hosts -e 29d

## ImageMagick

Convertir deux images en un seul pdf...

    :::console
    convert *.jpg -adjoin fichier.pdf

## Fuseau Horaire

Votre linux n'est pas sur le bon fuseau horaire?

    :::console
    tzselect
