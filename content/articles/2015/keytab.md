Title: Memo: Keytab Kerberos
Date: 2015-08-01 18:03
Author: Sebastien Badia
About_author: Engineer @RedHat, Puppet addict and Net Neutrality defender.
Category: Asrall
Slug: keytab

Un billet plus en mode mémo, ou comment créer un fichier [keytab](http://web.mit.edu/kerberos/krb5-devel/doc/basic/keytab_def.html) en vue de récupérer ultérieurement un token kerberos.

## keytab kerberos

Tout se déroule avec ktutils (paquet krb5-user), pour l'exemple, mon royaume est
*TOTO.FR*, mon user est *foo* et mon fichier keytab sera *foo.keytab*.

    :::bash
    ktutil
    >  addent -password -p foo@TOTO.FR -k 1 -e aes256-cts
    Password for foo@TOTO.FR:
    > wkt foo.keytab
    > quit

Il ne reste maintenant plus qu'a demander un ticket avec ce keytab:

    :::bash
    kinit -k -t foo.keytab foo

Et voila :-)
