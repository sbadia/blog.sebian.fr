Title: Premiers pas avec PostgreSql
Date: 2010-02-14 14:13
Author: Sebastien Badia
About_author: ASRALL Student
Category: Asrall
Tags: Serveur, Tips
Slug: postgresql
Modified: 2014-02-23 17:07

## Introduction

PostgreSQL est un système de gestion de base de données relationnelle et objet (SGBDRO). C'est un outil libre disponible selon les termes d'une licence de type BSD.

## Préliminaires

* Installer zlib: `zlib-dev`
* Puis readline: `libreadline-dev`
* Si ce n'est pas fait `buid-essential`

## Installation

Télécharger les dernières sources de postgresql sur le [site officiel](http://www.postgresql.org/) Puis dé-tarrer :p l'archive et se positionner dedans. `./configure` pour configurer (des options peuvent être passés. Enfin faire un `make` et en root un `make install`

## Configuration

Création d'un utilisateur Postgre avec `add user postgres`. Puis changement des droits `chown postgres /usr/local/pgsql/data` et Changement d'utilistateur`su -postgres`

Mise en place du cluster: `/usr/local/pgsql/bin/postgres -D /usr/local/pgsql/data` et Création d'une base `/usr/local/bin/createdb asrall`

## Démarrage

Se connecter avec l'utilisateur postgres, puis lancer la base avec cette commande `/usr/local/pgsql/ asrall`

## Arrêt propre

`pg-ctl -D /usr/local/pgsql/data stop -m fast`
