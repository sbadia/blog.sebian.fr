Title: Yet another tutorial about Let's Encrypt
Date: 2016-03-07 20:00
Author: Sebastien
About_author: Engineer @RedHat.
Category: Asrall
Tags: ASRALL, https, letsencrypt
Slug: letsencrypt

![Logo Let's Encrypt](//letsencrypt.org/images/letsencrypt-logo-horizontal.svg)

Voilà 1 million de certificats [Let's Encrypt](//letsencrypt.org/) délivrés (les certificats délivrés par [Let's Encrypt](https://crt.sh/?Identity=%25&iCAID=7395)); La littérature sur le sujet ne manque pas, mais je vais quand même en apporter une de plus, pour la partie compilation :-)

Pour rappel, Let's Encrypt, est un projet porté par l' « Internet Security Research Group » (ISRG), qui vise à automatiser, rendre accessible à tous, de manière ouverte et gratuite, des certificats SSL

# Génération

Nous allons ici, ne pas utiliser le client officiel; Principalement parce qu'il intègre trop de fonctionnalités (serveur web intégré, …), mais aussi parce qu'il ne réponds pas vraiment aux besoins de cet article (arborescence flexible, serveur nginx, …; et que c'est plus facile à lire un script de 200 lignes qu'un énorme client…)

Le client que nous allons utiliser est donc le [acme-tiny](https://github.com/diafygi/acme-tiny) (écrit en python). Lors de mes pérégrinations sur la toile (oui ok ça fait un peu vieillot, j'aurais pu dire « alors que je surfais sur le web », … :-D), je suis tombé sur ce script [letsencrypt.sh](https://github.com/lukas2511/letsencrypt.sh). Le coté FQDN à un endroit, et le rechargement lorsque les AltNames changent sont des features appréciables. Après c'est du bash, donc comme vous voulez :)

## Création des certificats

De mon coté, j'ai opté pour une arborescence de ce type (certificats générés dans un répertoire dédié, avec un utilisateur dédié).

```
$ mkdir -p /etc/letsencrypt/{certs,challenges,csr,pem,private}
/etc/letsencrypt/
├── certs
├── challenges
├── csr
├── pem
└── private
```

Il suffit donc alors de :

* Créer une clé pour le domaine en question
* Créer une demande de signature (CSR) en y incluant les noms DNS alternatifs
* Lancer le client (qui va se charger de créer un challenge) et signer si le challenge est ok.
* Télécharger et concaténer le certificat obtenu avec le certificat intermédiaire de Let's Encrypt

Le challenge sert ici à ce que let's encrypt vérifie que nous contrôlons bien le
domaine pour lequel nous demandons un certificat. Il faut d'ailleurs ajouter à
la configuration du serveur web, l'endroit où seront stockés ces challenges.

```nginx
location /.well-known/acme-challenge/ {
  alias /etc/letsencrypt/challenges/asrall.fr/;
  try_files $uri =404;
}
```

Coté certificat intermédiaire, ils sont disponibles sur le site de [Let's Encrypt](https://letsencrypt.org/certificates/).

![srg-keys](//letsencrypt.org/certs/isrg-keys.png)

Bon donc du coup ça donne cela dans un mini-script (pas super beau…)

```bash
#!/bin/bash
# bootstrap letsencrypt

account=$1
cert=$2
dns=$3

mkdir -p /etc/letsencrypt/{certs,challenges,csr,pem,private}

pushd /etc/letsencrypt
  if [[ ! -f "./private/${account}.key" ]]; then
    openssl genrsa 4096 > "./private/${account}.key"
  fi
  if [[ ! -f ./pem/intermediate.pem ]]; then
    wget -O - https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.pem > ./pem/intermediate.pem
  fi
  echo "##### ${cert} #####"
  if [[ ! -f "./private/${cert}.key" ]]; then
    openssl genrsa 4096 > "./private/${cert}.key"
  fi
  mkdir -p "./challenges/${cert}"
  openssl req -new -sha256 -key "./private/${cert}.key" -subj "/" -reqexts SAN -config <(cat /etc/ssl/openssl.cnf <(printf "[SAN]\nsubjectAltName=%s" "${dns}")) > "./csr/${cert}.csr"
  acme_tiny.py --account-key "./private/${account}.key" --csr "./csr/${cert}.csr" --acme-dir "/etc/letsencrypt/challenges/${cert}/" > "./certs/${cert}.crt"
  cat "./certs/${cert}.crt" ./pem/intermediate.pem > "./pem/${cert}.pem"
popd
```

Qu'il suffit de lancer comme ceci (pour l'exemple je génère un certificate
asral.fr avec comme domaines gérés asrall.fr et planet.asrall.fr (oui de la pub au passage))

```bash
$ bash bootstrap-letsencrypt.sh asrall asrall.fr 'DNS:asrall.fr,DNS:planet.asrall.fr'
##### asrall.fr #####
Parsing account key...
Parsing CSR...
Registering account...
Already registered!
Verifying planet.asrall.fr...
planet.asrall.fr verified!
Verifying asrall.fr...
asrall.fr verified!
Signing certificate...
Certificate signed!
```

Plutôt cool non? Il suffit alors d'adapter la configuration du serveur web, pour
prendre en compte ces certificats. Et passer tout en HTTPS! (dans notre cas,
c'est un nginx en reverse proxy qui gère le SSL et forward en HTTP sur une IP
privée).

```nginx
# Asrall
server {
  server_name asrall.fr planet.asrall.fr;
  rewrite ^(.*) https://$host$1 permanent;
}

# Asrall SSL
# DNS:asrall.fr,DNS:planet.asrall.fr
server {
  listen 443;
  ssl on;
  client_max_body_size 20M;
  server_name asrall.fr planet.asrall.fr asrall.sebian.fr;
  ssl_certificate /etc/letsencrypt/pem/asrall.fr.pem;
  ssl_certificate_key /etc/letsencrypt/private/asrall.fr.key;
  ssl_session_timeout 5m;
  ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
  ssl_ciphers ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA:ECDHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA;
  ssl_session_cache shared:SSL:50m;
  ssl_prefer_server_ciphers on;
  ssl_dhparam /etc/letsencrypt/dh4096.pem;
  ssl_ecdh_curve secp384r1;
  add_header Strict-Transport-Security max-age=15768000;
  resolver 127.0.0.1;
  location /.well-known/acme-challenge/ {
    alias /etc/letsencrypt/challenges/asrall.fr/;
    try_files $uri =404;
  }
  location / {
    proxy_pass       http://10.41.1.143;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-Proto https;
    proxy_set_header X-Forwarded-Ssl on;
  }
}
```

Pour la génération du dhparams (4096 bits c'est bien)

```bash
openssl dhparam -out dh4096.pem 4096
```

Et vous voila donc avec une super config et du HTTPS automatisé, on peut aller
faire un tour sur [imirhil](https://tls.imirhil.fr/https/asrall.fr) pour un
check de la conf et bien sûr pour pouvoir briller en société…

# Supervision

Bon c'est bien beau, mais avec tout ça les certificats sont valables que 90j
(oui mort à CertPatrol :-() mais pour le coup il va donc falloir superviser
tout cela.

## Via Certificate Monitor

Si vous utilisez le sympa [certificatemonitor](https://certificatemonitor.org/) ([code source](https://github.com/RaymiiOrg/certificate-expiry-monitor)) de Raymii, il suffit alors d'ajouter vos FQDN dans l'interface. Et ainsi recevoir une notification avant l'expiration de vos certificats.

## Via Checkmk

Sinon si vous avez déjà une bonne veille supervision à base de nagios ou checkmk ou compatible, il suffit d'ajouter les checks via le script `check_http`.

Dans la conf `main.mk` de checkmk:

```checkmk
# /etc/checkmk/main.mk
legacy_checks = [
  ## Asrall
  ( ( "check-certificate!asrall.fr", "Certificate Asrall - Letsencrypt", True), ['baloo.sebian.fr']),
  ( ( "check-certificate!planet.asrall.fr", "Certificate Planet Asrall - Letsencrypt", True), ['baloo.sebian.fr']),
]
```

Et ne pas oublier la `check_command` associée (on émet un warning lorsque que le certificat expire à J-30 et un critical à J-7)

```nagios
# /etc/checkmk/conf.d/commands_extra.mk
define command {
  command_name    check-certificate
  command_line    $USER1$/check_http -H $ARG1$ -C 30,7 --sni
}
```

# Renouvellement

Il existe des scripts de renouvellement automatique:

* [letsencrypt-renew](https://github.com/octopuce/octopuce-goodies/tree/master/letsencrypt-renew)
* [letsencrypt.sh](https://github.com/lukas2511/letsencrypt.sh)

Mais je ne sais pas encore quoi en penser, pour le moment je réagit lorsque que
le check passe en warning avec ce mini script bash.

```bash
#!/bin/bash

account='asrall'
certs='asrall.fr planet.asrall.fr'

pushd /etc/letsencrypt
  for cert in $certs
  do
    echo "##### ${cert} #####"
    acme_tiny.py --account-key ./private/labriqueinternet.key --csr ./csr/${cert}.csr --acme-dir /etc/letsencrypt/challenges/${cert}/ > ./certs/${cert}.crt
    cat ./certs/${cert}.crt ./pem/intermediate.pem > ./pem/${cert}.pem
  done
popd
systemctl restart nginx
```

# Chocolat

Même si le modèle des CA et bancal, il n'y a plus de raison maintenant de ne pas proposer du HTTPS partout!
