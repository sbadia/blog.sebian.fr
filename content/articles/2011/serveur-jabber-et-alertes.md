Title: Serveur jabber et alertes
Date: 2011-01-19 00:18
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: xmpp, jabber
Slug: serveur-jabber-et-alertes
Modified: 2014-02-23 17:07

Après être tombé sur le billet de [Cyrille Borne](http://www.cyrille-borne.com/index.php?post/2011/01/13/Faire-son-serveur-jabber-personnel-en-moins-de-5-minutes) concernant l'installation d'un serveur Jabber à base de Prosody en moins de 5-min, j'ai eu envie d'essayer :D (surtout à cause du down-time important de jabber.fr...)

Verdict, Prosody s'installe bien en 5min ;)

## Serveur Jabber

    :::console
    apt-get install prosody
    cd /etc/prosody/certs
    openssl req -new -x509 -days 365 -nodes -out "sebian.fr.cert" -keyout "sebian.fr.key"
    # Ajout dans /etc/prosody/prosody.cfg.lua
    Host sebian.fr
    # Et à la place du certif pour localhost.
    ssl = {
      key = "/etc/prosody/certs/monbeaudomaine.com.key";
      certificate = "/etc/prosody/certs/monbeaudomaine.com.cert";
    }

On ouvre le port 5222 en tcp en entrée et le port 5269 en tcp en entrée/sortie.

Et on ajoute un utilisateur

    :::console
    /etc/init.d/prospody start
    prosodyctl adduser foo@sebian.fr

## Alertes Jabber

Test du paquet sendxmpp (c'est du perl).  

    :::console
    apt-get install sendxmpp
    echo "notifications@sebian.fr mdp" > .sendxmpprc
    chmod 600 .sendxmpprc

Premier test  

    :::console
    df -h | sendxmpp -t -s "df sur le serveur jabber" seb@sebian.fr

Option -t pour utilisation de tls.

    :::console
    [23:13:29] notifications: Sujet : df server dev
    Sys. de fichiers    Taille  Uti. Disp. Uti% Monté sur
    /dev/hdv1              28G   18G  8,6G  68% /
    none                   16M  4,0K   16M   1% /tmp

Je vous laisse imaginer ce qu'on peux faire :D (hooks git, alertes scripts et même nagios !...)
