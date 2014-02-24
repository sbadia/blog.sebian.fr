Title: Synergy et c'est parti !
Date: 2010-05-25 23:55
Author: Sebastien Badia
About_author: ASRALL Student
Category: Tips
Tags: Debian, Tips
Slug: synergy-et-cest-parti
Modified: 2014-02-23 17:07

Oui d'accord... j'arrête avec mes noms de billets pourris ;)

Synergy est un petit logiciel permettant d'utiliser un seul clavier/souris pour différents systèmes d'exploitation ou machines.

Vous pouvez donc vous faire un dual screen avec deux ordinateurs différents, et là ou ça deviens super intéressant, c'est de lancer deux instances différentes d'un display manager et les "lier"/contrôler avec synergy...

Tout d'abord, le site du projet [synergy](http://synergy2.sourceforge.net/), la doc officielle est d'ailleurs très bien ;).

Synergy est compatible multi-plateforme ([Windows, Mac Os et bien sûr GNU/Linux](http://sourceforge.net/projects/synergy2/files/)).

Le logiciel fonctionne en client/serveur, et pour l'anecdote un client peut être aussi serveur, on peux donc s'amuser à contrôler autant d'écrans que l'on veux (testé en asrall cette année ;)), le potentiel de ce logiciel est vraiment impressionnant, autant que sa configuration...

D'ailleurs en parlant de configuration, prenons un exemle simple, j'ai deux machines différentes.

* Un Mac Os 10.4.11, hostname sebouriffe
* Une Debian, hostname triton

L'ip n'est pas utile ici, on va travailler avec les hostnames ;)

Pour sebouriffe, triton est à sa gauche, donc logiquement, pour triton, sebouriffe est à sa droite. Jusque là tout va bien?
Alors c'est bon vous avez fini !! Fichier de configuration dans */etc/synergy.conf*

    :::console
    section: screens
      sebouriffe:
      triton:
    end
    section: links
      sebouriffe:
        left = triton
      triton:
        right = sebouriffe
    end

Simple non ?

    :::console
    synergys
    synergys -f leFichierDeConf

Pour lancer le serveur, et pour le client ce n'est pas plus compliqué...

    :::console
    synergyc -f ipDuServeur

Et voila !!

Pour les frileux de la ligne de commande, il existe une petite interface  graphique rapide et efficace, [QuickSynergy](http://code.google.com/p/quicksynergy/).

J'espère que ça pourra vous être utile ;)
