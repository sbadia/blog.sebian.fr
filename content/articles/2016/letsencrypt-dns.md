Title: Let's Encrypt using DNS challenge
Date: 2016-07-08 18:00
Author: Sebastien
About_author: Network and System engineer
Category: Asrall
Tags: ssl , https ,dns, letsencrypt
Slug: letsencrypt-dns

![Logo Let's Encrypt](//letsencrypt.org/images/letsencrypt-logo-horizontal.svg)

On va encore parler de Let's Encrypt, non pas du fait que Comodo a essayé d'enregistrer la marque « Let's Encrypt » (oui rien que ça… ils ne doutent rien ces gens… voir [cet article](https://letsencrypt.org/2016/06/23/defending-our-brand.html)).

Mais on va parler de la possibilité de faire du *challenge/response* DNS pour la génération de nos certificats. En effet dans un [précédant article](//blog.sebian.fr/letsencrypt/), j'expliquais comment utiliser le client acme-tiny afin de générer des certificats SSL. Le soucis avec cette méthode (et le *challenge/response* en HTTP) c'est, comme son nom l'indique, qu'il utilise du HTTP(s); il faut donc obligatoirement avoir un serveur web qui va répondre aux challenges (afin de vérifier que nous avons bien le contrôle du domaine que nous souhaitons certifier).

Dans certains cas, il est nécessaire de générer des certificats sans disposer d'un serveur web (soit parce que le service est en interne et donc pas accessible depuis internet, ou alors c'est du mail ou autre… (dans mon cas)).

# Yet another script to manage Let's Encrypt...

Après [acme-tiny](https://github.com/diafygi/acme-tiny), voici [letsencrypt.sh](https://github.com/lukas2511/letsencrypt.sh), l'avantage de celui-ci est qu'il est ultra modulaire! Il supporte les *challenges* par http (classique), mais aussi par DNS (ajout d'un enregistrement txt dans la zone correspondante, voir la [doc](https://github.com/lukas2511/letsencrypt.sh/blob/master/docs/dns-verification.md) pour plus d'infos).

Donc nous disions, le truc cool c'est qu'il fonctionne via des hooks, et ils sont [nombreux!](https://github.com/lukas2511/letsencrypt.sh/wiki/Examples-for-DNS-01-hooks). [Lorraine Data Network](https://ldn-fai.net/) n'a pas encore de DNS contrôlé via une API, il faut donc faire un hook spécifique (en mode old-school via puppet/git :-D)

# Cas concret avec l'infra de Lorraine Data Network

```bash
./letsencrypt.sh -c -t dns-01 -d webmail.ldn-fai.net -d bender.ldn-fai.net -k ./hooks/ldn.sh
```

Le [hook en question](https://github.com/sbadia/letsencrypt.sh-ldn-dns/blob/master/hooks/ldn.sh), ce petit bout de bash fait donc:

- Mise à jour du dépot puppet LDN local
- Ajout de l'enregistrement TXT correspondant au domaine à certifier
- Mise à jour du serial de la zone
- Commit et push, puis lancement de puppet
- Attente d'une validation / certificat de la part de letsencrypt
- Nettoyage du TXT

Tout cela pour montrer que c'est assez trivial de tout automatiser avec ce système de hooks.
