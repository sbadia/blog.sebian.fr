Title: Tunnel Ssh Inversé
Date: 2010-08-16 23:41
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: Réseau, Ssh, Tips
Slug: tunnel-ssh-inverse
Modified: 2014-02-23 17:07

Oui on ne rigole plus ;)

Pour créer un tunnel inversé en ssh, depuis la machine où l'on crée le tunnel.

    :::console
    ssh -TR 1111:localhost:22 gnu

Sur la machine distante, pour se connecter au tunnel.

    :::console
    ssh -p 1111 localhost

La première commande ouvre un tunnel sur gnu vers la machine où le tunnel à été crée. (gnu est un host configuré dans le .ssh/config, ou toto@gnu.sebian.fr)

* Option -T pour ne pas ouvrir de shell.
* Option -R pour reverse (tunnel)
* Option -X pour forwarder le X

Des autres tips sont dispo [ici](http://wiki.sebian.fr/doku.php?id=tips:ssh)
