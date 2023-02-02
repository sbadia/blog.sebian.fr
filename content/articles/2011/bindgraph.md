Title: BindGraph
Date: 2011-04-24 20:48
Author: Sebastien
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: bind, graph, supervison
Slug: bindgraph
Modified: 2014-02-23 17:07

Je reprends l'écriture sur ce blog avec un billet sur l'installation de [BindGraph](http://www.linux.it/~md/software/bindgraph-0.2.tgz), le grapheur de requêtes dns.

J'avais à l'origine installé munin/munin-node sur mon serveur, mais avec une 15aine de vservers, munin posait des soucis de load au moment de la récupération des données.

Sur mon vserver dns, j'ajoute dans le fichier */etc/bind/named.conf.local*

    :::console
    logging {
      channel b_query.log {
        file "/var/log/bind9/query.log";
        print-time yes;
        severity info;
      };
      category queries {
        b_query.log;
      };
    };

C'est le moment d'installer le paquet.

    :::console
    apt-get install bindgraph

On remplace ensuite dans */etc/default/bindgraph* le path de notre log de query, et de même pour le service dans */etc/init.d/bindgraph*.

Le service peut être maintenant lancé.

    :::console
    /etc/init.d/bind9 reload
    /etc/init.d/bindgraph start
