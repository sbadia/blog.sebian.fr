Title: Vserver c'est le bonheur !
Date: 2010-02-14 14:39
Author: Sebastien Badia
About_author: ASRALL Student
Category: Tips
Tags: Debian, Serveur, Virtualisation
Slug: vserver-cest-le-bonheur
Modified: 2014-02-23 17:07


# Linux et la virtualisation

## Pour la petite histoire

Linux Vserver, fonctionne en isolateur, un isolateur est un logiciel permettant d'isoler l'exécution des applications dans ce que l’on appelle des contextes ou bien zones d'exécution. L'isolateur permet ainsi de faire tourner plusieurs fois la même application dans un mode multi-instance (plusieurs instances d’exécution) même si elle n’était pas conçue pour ça. Cette solution est très performante, du fait du peu d'overhead (temps passé par un système à ne rien faire d'autre que se gérer), mais les environnements virtualisés ne sont pas complètement isolés. La performance est donc au rendez-vous, cependant on ne peut pas vraiment parler de virtualisation de systèmes d’exploitation. Uniquement liés aux systèmes Linux, les isolateurs sont en fait composés de plusieurs éléments et peuvent prendre plusieurs formes.

## Installation

On installe d'abord le noyau spécifique Vserver (c'est l'inconvéniant)

    :::console
    apt-get install linux-image-2.6.26-2-vserver-686
    apt-get install util-vserver

### Création d'un vserver

Méthode avec debootstrap (pour debian ,ubuntu)

    :::console
    vserver vserver1 build -m debootstrap --context 42 -- hostname vserver1.mydomain.com --interface eth0:192.168.1.10/24  -- -d lenny -m http://ftp.de.debian.org/debian

Methode avec un template (Nimporte quelle distrib)

    :::console
    vserver centos build -m template --hostname centos.com  --interface eth0:192.168.1.42/24 -- -d centos5 -t /vservers/.templates/centos-5-i686-2008-07-09.tar.bz2

On spécifie donc le template avec le path complet. Si vous voulez des images (templates) j'en ai trouvé pleins sur http://mirrors.sandino.net/vserver/images/

### Utilisation

`vserver vserver1 start` Pour entrer dans le Vserver
`vserver vserver1 enter` L'arréter... `vserver vserver1 stop` Et le supprimer `vserver vserver1 delete` Un site très bien fait sur les [Vserver sur debian](http://linux-vserver.org/Installation_on_Debian).
