Title: Nom de domaine et ip Dynamique
Date: 2010-03-12 08:46
Author: Sebastien Badia
About_author: ASRALL Student
Category: Tips
Tags: sebian, Serveur, Tips
Slug: nom-de-domaine-et-ip-dynamique
Modified: 2014-02-23 17:07

Cette méthode fonctionne si vous avez acheté votre nom de domaine chez [OVH](https://www.ovh.com/fr/).

## Nom de domaine chez OVH

### Configuration des DNS

La méthode suivante permet de mettre à jour son ip dynamique directement dans la zone Dns. Pour ce faire, il suffit de vous rendre sur [l' interface de gestion Ovh](https://www.ovh.com/managerv3/). Sélectionner son nom de domaine dans la liste, et cliquer sur "domaine et DNS" puis sur "zone DNS".

On peux alors effacer toutes les entrées DNS, mise à part bien sûr les deux NS (Name Serveur). Une lecture du [tutoriel Ovh](http://guides.ovh.com/DynDns/) peut être utile...

On crée donc un enregistrement "DynHOST".

* Champ = .nom-de-domaine.tld
* Type = DynHOST
* Cible = Ip du moment`

Les identifiants DynHOST peuvent être crée en même temps, retenez bien le login/mdp que vous mettez ici, on s'en servira plus tard...

* Identifiant = ce-que-vous-voulez
* Zone = nom-de-domaine.tld
* Sous-domaine = *

Puis on peux créer un enregistrement CNAME, qui nous servira plus tard aussi.

* Champ = *.nom-de-domaine.tld
* Type = DynHOST
* Cible = nom-de-domaine.tld

**Note:** Il est important de mettre l'ip le moins de fois possible est si possible un CNAME "*" qui re-dirigera tout vers la machine (serveur), ainsi c'est sur le serveur que l'on gérera les sous domaines et autres...

**Note 2:** Pour un serveur de mail, il faut créer un enregistrement MX, une solution est de le faire comme ceci:

* Champ = mail.nom-de-domaine.tld
* Type = MX 1
* Cible = nom-de-domaine.tld

### Mis à jour avec DDclient

Il faut maintenant installer un petit soft qui vérifie que l'ip dans le manager est toujours la même que l'ip actuelle du serveur, pour ce faire ddclient fait très bien ce travail !

    :::console
    apt-get install ddclient

Répondez ce que vous voulez aux questions, de toute façon on modifiera la conf à la main (*/etc/ddclient.conf*) :p

Soit on commente et on active ce que l'on veux sont on colle ce qu'il y a ci-dessous à la place...

    :::console
    daemon=600
    # Vérifie l'ip toutes les 600 secondes
    syslog=yes
    # Log les maj dans syslog
    mail=root
    # Envoie le message de maj à root
    mail-failure=root
    # Si pb pendant l'update on averti root
    pid=/var/run/ddclient.pid
    # Enregistrement du fichier PID
    cache=/tmp/ddclient.cache
    # Fichier de Cache de ddclient
    ## Maj via un site Web
    use=web, web=checkip.dyndns.com/, web-skip='IP Address'
    ## Le login DynHost
    login=ce-que-vous-voulez
    ## Le Mdp allant avec...
    password=le-mot-de-passe
    ## Ici c'est l'interface de management pour nous Ovh, ne changez donc rien...
    protocol=dyndns2
    # Protocole par défaut
    server=www.ovh.com
    # Serveur d'Ovh
    ## Le nome de domaine updaté dynamiquement
    nom-de-domaine.tld

Une fois ce fichier enregistré, vous pouvez redémarrer le daemon (peut être activer dans "/etc/default/ddclient", mettre daemon à yes...)

    :::console
    /etc/ini.d/ddclient restart

Et voila vous avez maintenant un nom de domaine sur une ip dynamique, et tout ceci ce met à jour sans action de votre part, c'est pas magique?

## Sous-domaine Gratuit

On peux faire la même chose mais avec un nom de domaine gratuit, vous pouvez vous renseigner sur "dyndns" ou "no-ip.org"... L'avantage si vous avec une Neufbox ou une livebox c'est que celle-ci intègre un client dyndns directement dedans...
