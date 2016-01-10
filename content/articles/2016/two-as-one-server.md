Title: LDN BGP - Two AS one server
Date: 2016-01-11 11:53
Author: Sebastien Badia
About_author: Engineer @RedHat.
Category: Asrall
Tags: BGP, LDN, AS, ARN, routing, bird
Slug: two-as-one-server

Bon ok, on arrête tout de suite la similitude scabreuse…

# État actuel

Nous n'avons jamais trop communiqué sur ce sujet (si ce n'est dans nos
comptes-rendus de réunion, ou d'assemblé générale), cette configuration n'est
maintenant plus d'actualité puisque [Alsace Réseau Neutre](http://arn-fai.net/)
vole maintenant de ses propres ailes et même bien mieux, ils disposent d'un
quart de baie en data center!

# Introduction

Dans le cadre de [Lorraine Data Network](https://ldn-fai.net/) (Association pour
la défense d'un Internet Libre Décentralisé et Neutre, dont un des moyens
d'action est d'être fournisseur d'accès à Internet), pour des contraintes
techniques et de future indépendance, nous avons mis en place deux AS
(Autonomous System) sur une même machine physique.

Ce type de configuration n'est pas très commune, les autres solutions sont soit
de virtualiser. Mais pour des routeurs de bordure (recevant une full-view
(toutes les routes d'Internet)) ce n'est généralement pas conseillé, pour des
raisons de performance (les fameux paquets par secondes), soit on utilise deux
machines physiques :) mais nous sommes une petite association, et le but était
de lancer une association amie ARN ([Alsace Réseau Neutre](http://arn-fai.net/))
à moindre frais, et donc sur un seul serveur (celui-ci étant en Data Center).

Après de longues concertations et différents tests en bac à sable, nous avons
finalement opté pour une solution à base de bird (daemon libre de routage) dans
des namespaces réseau (netns).

# Coté implémentation

Nous gérons toutes nos configurations avec l'outil de gestion de confs Puppet,
nous avons donc développé un module pour bird,
[puppet-bird](https://github.com/sbadia/puppet-bird.git), celui-ci se charge
d'installer bird, désactiver le service/init par défaut et installer la
configuration bird{,6} et le script/unit d'init correspondant. Nous avons donc
deux processus bird par netns:

* bird-ldn et bird6-ldn dans le netns ARN
* bird-ldn et bird6-ldn dans le netns LDN

Les unit d'init ont été adaptés pour lancer les processus dans les netsns
correspondants.

    :::shell
    /sbin/ip netns exec $name_space /usr/sbin/bird -c $config_file -s $ctl_file >> "$stdout_log" 2>> "$stderr_log" &
    /sbin/ip netns exec $name_space /usr/sbin/bird6 -c $config_file -s $ctl_file >> "$stdout_log" 2>> "$stderr_log" &

Coté livraison BGP (Border Gateway Protocol) avec notre transitaire, nous avons un VLAN
par association, ce qui permet « d'enfouir » facilement l'interface dans le
namespace correspondant.

[Julien](http://ju.vg/) à même fait un super schéma récapitulant tout notre
configuration, celui-ci est nettoyé de toutes les [IP de
production](https://wiki.ldn-fai.net/med/images/e/eb/Infra-ldn-arn.pdf) ainsi
qu'une vidéo d'explication de notre [schéma d'adressage
réseau](https://ldn-fai.net/adressage-ipv6ipv4/).

Sinon pour la petite pub, [Gitoyen](http://gitoyen.net/) à publié sa (plutôt bien
faite) configuration BGP pour bird, c'est dispo sur la [forge de la Fédération
FDN](https://code.ffdn.org/gitoyen/bird-config/).

# Visualisation

Pour ce qui est des looking-glass et channel de contrôle, c'est tout pareil, il
suffit juste de prendre en compte la contrainte du namespace, et donc d'adapter
les commandes en conséquence.

Par exemple pour la commande ctl de brid:

    :::shell
    alias birdc-ldn='ip netns exec ldn birdc -s /var/run/bird-ldn.ctl'
    alias birdc6-ldn='ip netns exec ldn birdc6 -s /var/run/bird6-ldn.ctl'

Ou pour notre [looking-glass](http://lg.ldn-fai.net) qui utilise le
[looking-glass bird](https://github.com/sileth/bird-lg.git)

    :::shell
    DAEMON="/usr/local/lookingglass-ldn/lgproxy.py"
    DAEMONUSER="lookingglass-ldn"
    DEAMON_NAME="lookingglass"
    PID="/var/run/lookingglass.pid"
    /sbin/ip netns exec ldn /sbin/start-stop-daemon --background --name $DEAMON_NAME --start --quiet \
      --pidfile $PID --make-pidfile --chuid $DAEMONUSER --exec $DAEMON

# Performances et gestion

Pour ce qui est gestion, cela demande forcement plus de configuration (tout est
doublé), et il faut adapter les unit d'init et confs mais aussi les commandes de
contrôle et de visualisation (lg). Par contre une fois tout ceci derrière, la
gestion est exactement la même. Coté accès admin, les admins de confiance des
deux structures ont accès à la machine, et donc peuvent potentiellement influer
sur le routeur de l'association amie. (Ce n'est pas vraiment un problème dans
notre cas).

Coté performances le fait de faire tourner bird dans un netns au lieu de
directement sur l'hôte est complètement négligeable, par contre il faut
dimensionner sa machine en conséquence car elle accueille alors pas deux
full-views, pas 3 mais oui c'est bien 4 full-view mesdames et messieurs! (deux
en IPv6 et deux en IPv4).

      :::shell
      bird> s mem
      BIRD memory usage
      Routing tables:    172 MB
      Route attributes:  125 MB
      ROA tables:       8680  B
      Protocols:         124 kB
      Total:             297 MB

Niveau processus, 320m en virtuel et 310m en résidentiel
