Title: Supprimer un uid GPG
Date: 2013-10-10 23:03
Author: Sebastien
About_author: Cloud engineer @eNovance, Puppet addict and Net Neutrality defender.
Category: Tips
Tags: gpg
Slug: supprimer-un-uid-gpg
Modified: 2014-02-23 17:07

Je tentais de supprimer un uid de ma clé GPG en utilisant « deluid »
mais en vain.

    :::console
    # édition de la clé, et sélection du numéro de l'uid
    gpg2 --edit-key $KEYID
    # suppression
    deluid
    # sauvegarde
    save
    # et envoi
    gpg2 --keyserver hkp://pgp.mit.edu:11371 --send-key $KEYID

Jusque là tout semblait bon, mais au refresh (`gpg2 --refresh-keys`) l'uid en question était à nouveau ajouté à ma clé.

Je décide alors d'utiliser un outil graphique (genre `seahorse`), mais pareil… (il utilise `deluid`).

Ne trouvant pas de solution je décide de prendre le joker « appel un ami » l'ami me redirige vers `revoke` au lieu de `delete`.

Un petit tour dans le `man` et un RTFM plus tard :-)

> Note that it is not possible to retract a user id, once it has been
> send to the public (i.e. to a keyserver). In that case you better use
> revuid

On recommence avec `revuid` et ça juste marche !
