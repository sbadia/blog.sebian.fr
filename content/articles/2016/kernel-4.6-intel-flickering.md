Title: Bug plutôt gênant de flickering avec le noyau 4.6.x
Date: 2016-06-25 11:03
Author: Sebastien
About_author: Network and System Engineer.
Category: Asrall
Tags: system, linux, debian
Slug: kernel-4.6-intel-flickering

Avec la mise à jour du noyau Linux en 4.6.0 dans Debian, est apparu un bug bien
embêtant… L'écran de mon Thinkpad se met à clignoter… (ou flickering) de manière
aléatoire (et ça uniquement dans une session X window).

Si ça peut aider, voici quelques pointeurs!

## Correctif

Le soucis est connu, on trouve d'ailleurs pas mal de pointeur sur l'Internet! Le
problème est d'ailleurs patché et releasé dans la version 4.6.2 du noyau Linux.

    :::bash
    The default of 0 is 500us of link training, but that's not enough for
    some platforms. Decoding this correctly means we're using 2.5ms of
    link training on these platforms, which fixes flickering issues
    associated with enabling PSR.

## Liens sur les Internettes

* Première occurrence du bug, coté ArchLinux (09/06) <https://bugs.archlinux.org/task/49628>
* Le bug coté freedesktop: <https://bugs.freedesktop.org/show_bug.cgi?id=95176>
* [Merge du patch dans le trunk linux](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=03b7b5f983091bca17e9c163832fcde56971d7d1)
* Changelog 4.6.2 <https://www.kernel.org/pub/linux/kernel/v4.x/ChangeLog-4.6.2>

## Pour les impatient⋅e⋅s

Coté Debian, Salvator à releasé un nouveau paquet
[4.6.2-1](https://anonscm.debian.org/cgit/kernel/linux.git/commit/?id=86e78453315a430a49a84d5772123de321fcb660),
il est à l'écriture de ce billet disponible dans Debian unstable, ou sur snapshot.d.o:

* <http://snapshot.debian.org/package/linux/4.6.2-1/#linux-headers-4.6.0-1-amd64_4.6.2-1>

Sinon il faut juste attendre que 4.6.2-1 arrive dans testing :)
