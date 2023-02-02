Title: Gestion du carnet d'adresses avec Mutt
Date: 2014-05-22 23:00
Author: Sebastien
About_author: Cloud engineer @eNovance, Puppet addict and Net Neutrality defender.
Category: Asrall
Tags: Mutt, Abook, Notmuch, Nottoomuch
Slug: mutt-nottoomuch

Yop, ça va parler gestion de carnet d'adresse avec ce superbe MUA moderne qu'est mutt. Bon je passe tout de suite les alias via mutt :-)

# Abook

Abook est un petit logiciel en curses pour la gestion de votre carnet d'adresses, il possède de nombreux scripts d'import, et sont interface est plutôt intuitive (possibilités de rentrer des infos détaillées par contact, etc)

Coté intégration à mutt c'est assez simple.

    :::bash
    # ~/.muttrc
    macro index,pager  a "<pipe-message>abook --add-email-quiet<return>" "Ajouter cet expéditeur dans Abook"
    set query_command= "abook --mutt-query '%s'"
    bind editor  <Tab> complete-query

Il suffit donc d'appuyer sur « a » pour ajouter une adresse dans abook (mail courant), et pour écrire, il suffit de taper les premières lettres puis tab.

Pratique, mais ça ressemble beaucoup aux alias mutt pour l'apprentissage… Je suis récemment tombé sur autre chose!

# Nottoomuch

[Nottoomuch](https://github.com/domo141/nottoomuch) à quant lui le gros avantage d'apprendre automatiquement les adresses qu'indexe notmuch. Un gros avantage donc! (Toutes les adresses auxquelles vous avez envoyé ou reçu du mail sont dans votre carnet d'adresses)

    :::bash
    bind editor <Tab> complete-query
    set query_command="$HOME/.mutt/ntmw.sh %s"
    set query_format="%t %-25.24n %a %e"

Pour plus de précisions sur le [query\_format](http://durak.org/sean/pubs/software/mutt/reference.html#query-format)

Et pour le wrapper sur nottoomuch (ntmw.sh):

    :::bash
    #!/usr/bin/env sh
    # nottoomuch-addresses.sh wrapper
    $HOME/.mutt/nottoomuch-addresses.sh "$1" \
      |sed -s 's/\(.*\) \(<.*\)/\2\   \1/'\
      |sed -s 's/\"//g'\
      |sed -s '/buzz+.*/d'\

Il ne reste plus qu'a lier *nottoomuch-addresses.sh --update* dans votre config offlineimap (en hook), et le tour est joué.

L'article est bien inspiré du blog de [tshirtman](http://blog.tshirtman.fr/tags/nottoomuch) merci!
