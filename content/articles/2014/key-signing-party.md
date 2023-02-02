Title: KeySigning Party
Date: 2014-05-22 20:00
Author: Sebastien
About_author: Cloud engineer @eNovance, Puppet addict and Net Neutrality defender.
Category: Asrall
Tags: GPG, KeySigning, PDF
Slug: signing-party


Hello, un petit tips bien sympa pour préparer au mieux vos [signing-party](https://en.wikipedia.org/wiki/Key_signing_party), ou pour distribuer facilement votre fingerprint…

*gpg-key2ps* permet de formater votre clée pour pouvoir l'imprimer facilement, le paquet est dispo dans [signing-party](https://packages.debian.org/jessie/signing-party) si vous êtes sur du Debian-like.

Coté utilisation, c'est relativement simple.

    :::bash
    gpg-key2ps -p A4 0x14A452D8 > 14A452D8.ps
    ps2pdf 14A452D8.ps
    evince 14A452D8.pdf

Changez **14A452D8** par votre keyid bien sûr ;-).

Bonne signing-party!
