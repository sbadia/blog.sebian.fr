Title: Statusnet sur son propre serveur
Date: 2011-06-13 14:20
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Installation Tips
Tags: statusnet, xmpp
Slug: statusnet-sur-son-propre-serveur
Modified: 2014-02-23 17:07

Un petit billet pour décrire l'installation d'un serveur statusnet (utilisé par identi.ca entre autres).

## Partie Web

Si votre serveur web est déja installé faites juste un

    :::console
    apt-get install php5-curl

pour installer le module curl nécessaire.

Sinon pour tout installer

    :::console
    apt-get install apache2 mysql-server php5 php5-curl

On continue avec l'installation depuis les sources

    :::console
    cd /var/www/
    wget http://status.net/statusnet-0.9.7fix1.tar.gz
    tar xvzf statusnet-0.9.7fix1.tar.gz
    mv statusnet-0.9.7fix1 statusnet
    chown -R www-data:www-data statusnet/

Et pour finir on active les rewrites rules avec

    :::console
    mv htaccess.sample .htaccess

en prenant soin de modifier la *RewriteBase*
    :::apache
    RewriteBase /

On peux rajouter dans le *config.php* la ligne suivante
    :::php
    echo "$config['site']['fancy'] = true;" >> config.php

## Partie Base de donnée

Nous allons utiliser mysql pour le stockage

    :::console
    mysql -u root -p

Et on crée la base de données

    :::mysql
    create database dbnotifs; GRANT ALL on dbnotifs.* TO 'statususer'@'web.example.fr' IDENTIFIED BY '****';

## Configuration

On se connecte maintenant sur [http://fqdn/install.php](http://fqdn/install.php) et on réponds aux questions ;) à la suite de cela notre installation est fonctionnelle, mais on ne peux poster que avec le client web, ou avec un client lourd.

## Post par xmpp

Rien de plus simple ! et c'est tellement pratique...

### Coté serveur jabber

Si vous avec un *prosody*, la commande se limitera à

    :::console
    prosodyctl adduser bot@example.fr


### Coté statusnet

Ajoutez dans la *config.php*

    :::php
    cat << EOF >> /var/www/statusnet/config.php
    $config['xmpp']['enabled'] = true;
    $config['xmpp']['server'] = 'example.fr';
    # XMPP server name $config['xmpp']['host'] = NULL;
    # Only set if different from server
    $config['xmpp']['port'] = 5222;
    $config['xmpp']['user'] = 'bot';
    # set to what ever user name is registered on XMPP server
    $config['xmpp']['encryption'] = true;
    $config['xmpp']['resource'] = 'uniquename';
    $config['xmpp']['password'] = '****';
    $config['xmpp']['debug'] = false;
    $config['queue']['enabled'] = true; EOF

Puis il ne reste plus qu'a lancer le daemon.

    :::console
    sh /var/www/statusnet/scripts/startdaemons.sh

### Utilisation du bot

Pour utiliser le bot, il suffit de l'ajouter dans vos contacts jabber, de lui envoyer "help" et de valider sont jabberid sur le lien répondu ;)

Bon hack !
