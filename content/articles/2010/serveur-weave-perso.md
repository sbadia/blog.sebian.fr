Title: Serveur Weave Perso
Date: 2010-09-29 02:02
Author: Sebastien
About_author: ASRALL Student
Category: Tips
Tags: Debian, Mozilla, Serveur, Tips
Slug: serveur-weave-perso
Modified: 2014-02-23 17:07

Hello, aujourd'hui un petit billet, pour détailler l'installation d'un serveur [weave](https://wiki.mozilla.org/Labs/Weave/Sync/1.0/Setup) perso.

Pourquoi me direz vous ? Parce que je ne prends pas tout le temps le portable du boulot quand je rentre chez moi (le sync est très pratique), et parce que je ne voulais pas que mes données aillent chez Mozilla, oui je suis sans doute parano ! Enfin pour le challenge ;)

J'utilise donc la version **"Minimal Server"** dispo [ici](http://people.mozilla.org/~telliott/weave_minimal.tgz), l'installation est assez déconcertante de facilité !

    :::console
    tar xvzf weave_minimal.tgz
    mv weave_minimal /var/www/weave
    chown httpd. /var/www/weave

Le serveur minimale utilise sqlite pour stocker les données, il vous faut donc sur debian le paquet suivant.

    :::console
    apt-get install php5-sqlite

Puis rajouter la ligne suivant dans sa conf apache.

    :::apache
    Alias /weave /var/www/weave/index.php

L'utilisation du https est impérative, selon le wiki elle n'est pas obligatoire, mais je n'ai pas réuissi à établir de syncro sans... (erreur).

Il nous reste plus qu'a redémarrer apache et créer un utlisateur (rdv dans le repertoire weave).

    :::console
    /var/www/weave php create_user
    > (c)reate, (d)elete or change (p)assword: c
    > Please enter username: toto
    > Please enter password: totopass
    > toto created

Dernière étape, on télécharge le [plugin](https://addons.mozilla.org/en-US/firefox/addon/10868/), et pour la conf, il suffit de donner "j'utilise déja"

* Se connecter à => Utiliser un serveur perso
* Url => https://toto.com/weave/
* Utilisateur => toto
* Pass => totopass

On peux vérifier ;)

    :::console
    du -sh /var/www/weave/
    > 2.8M /var/www/weave/

Enjoy !
