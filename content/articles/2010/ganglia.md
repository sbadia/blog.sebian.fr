Title: Ganglia
Date: 2010-02-14 14:36
Author: Sebastien Badia
About_author: ASRALL Student
Category: Tips
Tags: Debian, Serveur, Supervision
Slug: ganglia
Modified: 2014-02-23 17:07

Vous voulez faire du monitoring sur votre serveur, ou plutôt sur votre cluster ?
Utilisez ganglia, il utilise RRDtools, et il est vraiment bien fait !

## Phase préparatoire

On commence par installer la librairie Gd et rrdtools

    :::console
    apt-get install rrdtool librrds-perl librrd2-dev php5-gd ganglia-monitor gmetad librrd2-dev libapr1-dev libexpat1-dev python-dev

## Installation

Il faut ensuite télécharger le tarball sur [le site de Ganglia](http://ganglia.sourceforge.net/), car j'ai pas entendu que du bien du paquet. Enfin d'au autre coté je ne l'ai pas testé, donc je ne dirais rien ;)

    :::console
    wget lien-ganglia-du-moment
    tar xvzf tarball-ganglia-du-moment
    cd dossier-ganglia-du-moment

Bien sur vous remplacez "ganglia du moment" par la version actuelle...

Ensuite un "./configure --help" nous premet de voir toutes les options, mais pour une installation "basique" faites un

    :::console
    ./configure --enable-gexec --with-gmetad

Et si tout se passe bien ceci apparaît dans la console le logo...

On fait donc un "make" suivi d'un "make install". Enfin on peux copier le contenu du repertoire "web" dans l'arbo. du serveur web.

    :::console
    mkdir /var/www/ganglia
    cp -r web/* /var/www/ganglia

## Rendu

Et voila! pour admirer le travail, vous pouvez vous rendre sur http://votre-serv/ganglia/
