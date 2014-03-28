Title: Debian et CACert.org
Date: 2014-03-28 00:31
Author: Sebastien Badia
About_author: Cloud engineer @eNovance, Puppet addict and Net Neutrality defender.
Category: Tips
Tags: Debian, Certs, CACert.org
Slug: debian-cacert

Le [23 février dernier](http://anonscm.debian.org/gitweb/?p=collab-maint/ca-certificates.git;a=commit;h=dc63c085c390ee126f9100fee23c902d610a9bab), Debian à décidé de ne plus embarquer le certificat root de [CACert.org](http://cacert.org/) dans son paquet [ca-certificates](http://packages.qa.debian.org/c/ca-certificates.html).

Nous allons pas parler ici de cette décision et de son large impact, je vous laisse lire le bon article de [lwn.net](http://lwn.net/SubscriberLink/590879/cc288a6be9b64e4d/) à ce sujet, ou les récents threads sur les listes Debian ([bug](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=718434) ou [thread](https://lists.debian.org/debian-devel/2014/03/msg00375.html)); Non, nous allons parler de créer un .deb incluant nos propres certificats root.

Le paquet ca-certificates, contient tout le nécessaire pour builder ce paquet, il suffit de faire un tour dans */usr/share/doc/ca-certificates/example* (il y a un README).

Essayons donc, avec pour exemple, les CA de CACert.org tient :-)

    :::console
    # On copie l'aro dans notre home, pour la modifier
    cp -a /usr/share/doc/ca-certificates/examples/ca-certificates-local ~
    cd ~/ca-certificates-local
    # Puis on supprime le certificat de test
    rm local/Local_Root_CA.crt
    # Et ajout des certificats CACert.org
    wget http://www.cacert.org/certs/root.crt -O local/root.crt
    wget http://www.cacert.org/certs/class3.crt -O local/class3.crt

Vérification des SHA1 cf. [http://www.cacert.org/index.php?id=3](http://www.cacert.org/index.php?id=3)

* root: 13:5C:EC:36:F4:9C:B8:E9:3B:1A:B2:70:CD:80:88:46:76:CE:8F:33
* class3: AD:7C:3F:64:FC:44:39:FE:F4:E9:0B:E8:F4:7C:6C:FA:8A:AD:FD:CE

Et c'est parti, (on peux modifier les infos dans debian/{changelog,control}) comme son nom, et la description. Une fois fini, pour builder le paquet il suffit de lancer

    :::console
    dpkg-buildpackage

Et voila :-)
