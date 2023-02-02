Title: Re-root android suite à une mise à jour (4.3) (adb « error: closed »)
Date: 2013-08-12 18:50
Author: Sebastien
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: android
Slug: re-root-android-suite-a-une-mise-a-jour-4-3-adb-error-closed
Modified: 2014-02-23 17:07

Un petit billet rapide, en passant, pour re-rooter son androphone suite à une mise à jour

    :::console
    sudo apt-get install android-tools-adb android-tools-fastboot

On commence par rebooter en recovery (ou bouton power + volume-down sur un nexus).

    :::console
    sudo adb reboot recovery
    sudo adb sideload UPDATE-SuperSU-v1.50.zip
    > error: closed

Et là c'est le drame, mais il suffit juste de passer adb en usb (encore fallait il le savoir :-))

    :::console
    sudo adb usb
    > restarting in USB mode
    sudo adb sideload UPDATE-SuperSU-v1.50.zip
    > sending: 'UPDATE-SuperSU-v1.50.zip'  100%

Et voila !
