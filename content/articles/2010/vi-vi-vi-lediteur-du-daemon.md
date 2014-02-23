Title: Vi Vi Vi l'éditeur du daemon ;)
Date: 2010-05-10 22:11
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: Debian, Supervision, Tips
Slug: vi-vi-vi-lediteur-du-daemon
Modified: 2014-02-23 17:07

Une petite compilation des astuces Vim, qui me sont très utiles.

## Effacements

Effacer un mot (curseur sur le mot en question)

    :::vim
    dw

Effacer du curseur jusque à la fin de ligne.

    :::vim
    d$

## Remplacements

Utilisation des fonctions Sed de Vim.

Avec un motif sur tout un fichier

    :::vim
    :%s/ancien/nouveau/g

Seulement sur la ligne du curseur

    :::vim
    :s/ancien/nouveau/g

Seulement jusqu'à la première occurrence sur la ligne.

    :::vim
    :s/ancien/nouveau

## Ajouts

Ajouter un caractère ou plus sur n lignes. Ajouter les caractères en question en début de ligne.

Sélectionner en mode bloc, taper un *I* majuscule, puis les caractères et enfin *Echap*

    :::console
    Ctrl-V -> I -> caractères -> Echap

Ajouter les caractères en question en fin de ligne.

Sélectionner en mode bloc, taper un *$I* majuscule, puis les caractères et enfin *Echap*

    :::console
    Ctrl-V -> $I -> caractères -> Echap

## Dictionnaire

Si vous avez un dictionnaire placez le dans *.vim/spell*, ou laisser vim le télécharger...

Activation de la correction orthographique.

    :::vim
    :set spell spelllang=fr
    :setlocal spell spelllang=fr

Apprendre / Ajouter un mot au dictionnaire

    ::vim
    zg

Parcours des mots "faux"

Suivant `]s`

- Précédant `[s`
- Liste pour choisir (mode dictionnaire) `z=`

## Mise en forme

Mettre tout le document sur 80 colonnes (création d'une map)

    :::vim
    nmap  ma1GgqG`a
    gqap

Ou si on viens de commencer le document (retour à la ligne automatique à 80)

    :::vim
    :set tw=80

## Environement

Ouvrir tous les fichiers *.tex* dans plusieurs onglets.

    :::console
    vim -p *.tex

(Navigation avec Page-Up/Page-Down)

Ouvrir un nouveau document depuis un vim déjà lancé

    :::vim
    :tabnew

Ouvrir un document existant depuis un vim déjà lancé

    :::vim
    :tabedit

"Sliter" deux document dans la même fenêtre vim.

* En Horizontal `:split fichier`
* En Vertical `:vsplit fichier`

Insérer le résultat d'une commande dans le document vim courant

    :::vim
    :r! cmd
