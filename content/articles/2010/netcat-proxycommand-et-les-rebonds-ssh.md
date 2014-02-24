Title: Netcat, ProxyCommand et les rebonds Ssh
Date: 2010-08-16 23:26
Author: Sebastien Badia
About_author: ASRALL Student
Category: Tips
Tags: Réseau, Serveur, Ssh
Slug: netcat-proxycommand-et-les-rebonds-ssh
Modified: 2014-02-23 17:07

[Netcat](http://netcat.sourceforge.net/) est un petit utilitaire permettant d'ouvrir des connexions réseau, UDP ou TCP. Il est aussi appelé le « couteau suisse du TCP/IP » ! C'est pour dire ;)

Nous allons voir ici son efficacité pour le rebond des connexions ssh, tout se passe dans le fichier "*.ssh/config*".

On configure un host tout à fait normalement...

    :::console
    Host gnu
      Hostname gnu.sebian.fr
      User seb
      Port 66
      IdentityFile /home/%u/.ssh/id_dsa_gnu

Cet host sera donc la première étape de notre connexion, pour arriver à notre fin, on configure le deuxième host, et ça ce passe toujours dans le *.ssh/config* de notre machine locale ;)

    :::console
    Host bsd
      Hostname bsd.sebian.fr
      User seb
      ProxyCommand ssh gnu "nc -q 0 `basename %h` %p"

Et voila notre configuration éffectué !

Maintenant un `ssh bsd`

Donc on est sur la machine A (laptop) avec l'utilisateur seb, dans le *.ssh/config* de seb il y a les deux host de configuré B pour le host **gnu** et C pour le host **bsd**

Si depuis A je fais **ssh gnu** il se retrouve sur gnu.sebian.fr.

Maintenant si je fais **ssh bsd** la proxycommand se connecte à **gnu** puis balance le netcat qui lui se connecte à basename qui est **bsd** en l'occurrence.

On se retrouve bien sur **bsd** tout en étant passé par **gnu** :)

Ce type de configuration peux commencer à devenir intéressant en utilisant des wildcards :)

    :::console
    Host *.root
      User rootseb
      ProxyCommand ssh gnu "nc -q 0 `basename %h .root` %p"
      IdentityFile /home/%u/.ssh/id_dsa_rootseb

Ici on utilise directement le dns pour résoudre notre étoile

    :::console
    ssh dns.root

Bon hack ;)
