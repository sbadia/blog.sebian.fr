Title: Memo: Monter une image qcow2
Date: 2016-06-18 11:03
Author: Sebastien Badia
About_author: Network and System Engineer.
Category: Asrall
Tags: system, qemu
Slug: qemu-nbd-qcow2

Un billet plus en mode mémo, ou comment monter une image qcow2/qcow en vue d'accéder au système de fichier qu'il contient.

## Utilisation de qemu-nbd

Dans mon cas, j'avais besoin d'accéder à une machine virtuelle (au format qcow2)
mais sans la démarrer, il suffisait donc de monter le qcow2 et d'accéder direct
au filesystem (un peu plus compliqué que dans le cas d'un lvm, mais ça reste
simple).

    :::bash
    modprobe nbd max_part=8
    qemu-nbd -c /dev/nbd0 /srv/images/ma-super-vm.qcow2
    mount /dev/nbd0p1 /mnt

On fait ce qu'on veux faire avec la partition ainsi montée… et une fois fini,

    :::bash
    umount /mnt
    qemu-nbd -d /dev/nbd0

Et voila :-)
