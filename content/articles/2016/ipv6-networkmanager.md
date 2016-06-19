Title: IPv6, NetworkManager et vie privée
Date: 2016-06-19 14:02
Author: Sebastien Badia
About_author: System and network administrator.
Category: Asrall
Tags: IPv6, NetworkManager, Privacy
Slug: ipv6-networkmanager-privacy

![noplacelike](//blog.sebian.fr/images/noplacelike-v6.jpg)

Sur la plus part des réseaux IPv6, les adresses sont crées/distribuées via [SLAAC
(Stateless address autoconfiguration)](https://en.wikipedia.org/wiki/IPv6_address#Stateless_address_autoconfiguration)

En pratique ça fonctionne comme cela:

* L'host envoie une `router solicitation request` (salut, ça à l'air cool ici, il y a des routeurs dans le coin?)
* Le routeur réponds avec un préfixe (salut, c'est moi le routeur, ton adresse devra commencer par ce préfixe)
* L'host utilise alors le préfixe et l'adresse MAC de son interface pour générer une adresse IPv6

Le format des adresses générées par l'host est aussi appelé
[EUI-64](https://en.wikipedia.org/wiki/IPv6_address#Modified_EUI-64). Pour plus
de détails à propos de ce procédé, la page de l'IEEE explique tout, le wiki
d'ArchLinux est pas mal aussi!


* [IEEE's guidelines for EUI-64](https://standards.ieee.org/develop/regauth/tut/eui64.pdf)
* [ArchLinux IPv6](https://wiki.archlinux.org/index.php/IPv6)

# D'un point de vue, sécurité et vie privée

Bon SLAAC, ça marche bien et c'est pratique, mais ça permet de quand même leaker
pas mal d'informations à propos du périphérique qu'on utilise… (avec l'adresse
MAC, et une recherche OUI-Search, on connais facilement le périphérique), on
peut aussi effectuer du tracking assez précis…

Il est aussi possible d'en extraire des informations de localisation assez
précises.

# Adresses temporaires

Mais comme disait l'autre, en informatique, rien n'est impossible! Il existe
donc un système d'[adresses
temporaires](https://en.wikipedia.org/wiki/IPv6_address#Temporary_addresses).
Pour Apple et Windows, je ne sais pas trop, mais pour la mojorité des Linux ce
n'est pas activé par défaut.

On peut l'activer coté système, via `sysctl`:

    :::bash
    # Do not use a temporary address
    net.ipv6.conf.all.use_tempaddr = 0
    # Set a temporary address, but do not make it the default
    net.ipv6.conf.all.use_tempaddr = 1
    # Set a temporary address and make it the default
    net.ipv6.conf.all.use_tempaddr = 2

Via NetworkManager, c'est presque la même chose, et on peut activer les adresses
temporaires via `nmcli` via l'attribut ipv6.ip6-privacy.  Pour les interfaces
filaires, on spécifie directement l'interface, et pour les connexions wifi,
c'est par contre par point d'accès (via le nom du point d'accès).

    :::bash
    nmcli con modify eth0 ipv6.ip6-privacy 2
    nmcli connection modify courgette ipv6.ip6-privacy 2

**courgette** étant le nom d'un point d'accès wifi.

L'activation est alors automatique, l'adresse MAC de l'interface n'est alors
plus utilisé pour « construire » l'adresse IPv6 globale de l'interface.

    :::bash
    ip a s eth0

# Pour briller en société

Les adresses temporaires sont construites en se basant sur l'adresse MAC et une
chaine de caractères aléatoire, l'adresse assignée change alors à chaque fois.
Ce n'est donc pas à envisager si vous avez besoin d'accéder à votre système par
IPv6 (ip renseignée dans un DNS, serveur, ou device non-mobile).
