Title: Debian sur un Dell E6510
Date: 2010-09-13 23:25
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: Dell E6510, Debian
Slug: debian-sur-un-dell-e6510
Modified: 2014-02-23 17:07

Je viens de recevoir au boulot mon nouveau portable, un Dell E6510, une belle bête !

* Intel(R) Core(TM) i5 CPU M 540 @ 2.53GHz
* Hdd de 500Go
* 4 Go Ddr3 de Ram
* 15.6" @ 1920x1080
* Nvidia Quadro 3100M

Vous me direz que du bonheur ?

Oui, enfin pas tout à fait, sinon pas d'article ;)

Et oui sous debian, ubuntu le driver "nouveau" fait des siennes avec l'µc, symptômes, un écran noir au Boot après l'installation, framebuffer ?

Non non nouveau ;)

Je reboot donc après l'install de debian sur un live-cd, et je me chroot dans mon install toute fraîche :)

J'ajoute les dépôts non-free à mon source.list

    :::console
    deb http://ftp.debian.org/debian/ squeeze main contrib non-free
    deb-src http://ftp.debian.org/debian/ squeeze main contrib non-free

J'installe et je lance

    :::console
    apt-get install nvidia-xconfig && nvidia-xconfig

Une petit édition du fichier crée, pour remplacer

    :::console
    Section "Device"
      Identifier     "Device0"
      Driver         "vesa"
      VendorName     "NVIDIA Corporation"
    EndSection

Par ça (support haute résolution).

    :::console
    Section "Screen"
      Identifier     "Screen0"
      Device         "Device0"
      Monitor        "Monitor0"
      DefaultDepth    24
      SubSection     "Display"
        Depth         24
        Modes        "1920x1080@60"
      EndSubSection
    EndSection

Puis une fois ceci fait, on peux installer le driver comme indiqué sur le [Wiki debian](http://wiki.debian.org/NvidiaGraphicsDrivers)

    :::console
    apt-get install module-assistant nvidia-kernel-common
    m-a auto-install nvidia-kernel-source
    apt-get install nvidia-settings && nvidia-settings

Je configure mon dual-screen, enregistre et reboot :)

Et magie :D C'est fonctionnel :D

Enjoy !
