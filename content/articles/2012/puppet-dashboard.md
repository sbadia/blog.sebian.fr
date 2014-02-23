Title: Puppet dashboard
Date: 2012-01-11 01:37
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: puppet
Slug: puppet-dashboard
Modified: 2014-02-23 17:07

Petit retour d'expérience sur mon utilisation de puppet/puppet dashboard.

Voila maintenant environ 2 mois que j'utilise puppet sur mon serveur perso, outre l'installation classique (puppetmaster/client) le tout signé par certificat (puppetca)

(voir [Puppet install by Deimos](http://www.deimos.fr/blocnotesinfo/index.php?title=Puppet_:_Solution_de_gestion_de_fichier_de_configuration) et [Puppet install by foaa](http://blog.foaa.de/2010/07/playing-with-puppets-on-debian/)).

J'ai rajouté l'implémentation de GIT pour la tracibilité des recettes, et des tâches [Capistrano](https://github.com/capistrano/capistrano/wiki/Documentation-v2.x) pour la "colle" entre tout ceci, et puppet Dashboard (module de visualisation).

Installation du [dashboard](http://sebian.fr/conf/puppet-dashboard.txt). par recette puppet bien sûr ;) (version 1.2.3 de puppetlabs)

Pour la suite ça se passe dans dans */usr/share/puppet-dashboard*, le Rakefile permet d'ajouter des noeuds/classes en ligne de commande (rake node:add, nodeclass:add), sinon vous pouvez vous rendre sur l'interface web, et créer vos noeuds depuis (les workers sont lancés par la recette).

Pour le reporting, il suffit d'activer (report = true sur les clients) et pour l'inventaire autoriser le puppetmasterd à accéder aux facts

    :::puppet
    path /facts
    auth no
    method find
    allow *

![puppet dashboard]({filename}/images/dashboard.png)
