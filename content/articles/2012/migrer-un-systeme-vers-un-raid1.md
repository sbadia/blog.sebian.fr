Title: Migrer un système vers un Raid1
Date: 2012-01-12 23:34
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: lvm, mdadm, raid
Slug: migrer-un-systeme-vers-un-raid1
Modified: 2014-02-23 17:07

Le but de la manip est de passer d'une installation fonctionnelle en LVM  sur un seul disque à une installation toujours avec LVM mais sur un raid  1 (sur deux disques).

## Introduction

Dans la suite on admet que l'installation initialle est telle que :

    :::console
    /dev/sda:
        /sda1 -> /boot (200Mo)
        /sda2 -> old-server (reste du hdd) root tmp var swap

## Mise en place

On commence par copier la table de partition sur le deuxième disque

    :::console
    sfdisk -d /dev/sda | sfdisk /dev/sdb

Puis avec mdadm (raid soft) on crée nos deux arrays, nous allons volontairement ne mettre qu'un seul disque dans chaque array.

Md0 sera notre raid pour le */boot*

    :::console
    mdadm --create /dev/md0 --level 1 --raid-devices=2 missing /dev/sdb1
    mkfs.ext2 /dev/md0

Et Md1 le raid pour notre vg

    :::console
    mdadm --create /dev/md1 --level 1 --raid-devices=2 missing /dev/sdb2

On crée ensuite le pv sur */dev/md1* et le vg dans la foulée

    :::console
    pvcreate /dev/md1 && vgcreate vg-server /dev/md1

Puis nos lv et le filesystem (on répète l'opération pour les autres) :)

    :::console
    lvcreate -n root -L 6g vg-server
    mkfs.ext3 /dev/vg-server/root

## Copie du système actuel

On commence par monter notre nouveau *boot*

    :::console
    mount -t auto /dev/md0 /mnt/

et on lance la copie après si nécessaire avoir monté le fs d'origine en loop

    :::console
    mount -o loop /boot /root/boot
    cp -vdprx /root/boot /mnt

Même opération pour nos lv

    :::console
    mount -t auto /dev/vg-server/root /mnt
    mount -o loop /dev/old-server/root /root/root
    cp -vdprx /root/root /mnt

## Avant le reboot

Avant de rebooter il faut penser à modifier le fstab (/dev/md0 pour boot  et le nouveau vg pour les autres moint-points).

    :::vim
    :%s/sda1/md0/g
    :%/old-server/vg-server/g

Il faut ensuite régénérer l'intird

    :::console
    update-initramfs -u -k `uname -r`

et bien sûr à installer grub sur  notre nouveau disque (grub-install).

Et enfin créer un fichier de configuration pour mdadm.

    :::console
    mdadm  --detail --scan >> /mnt/etc/mdadm/mdadm.conf

## Touche finale

Après reboot (si tout s'est bien passé), on peux intégrer l'ancien disque dans l'array :)

    :::console
    mdadm --add /dev/md0 /dev/sda1 && mdadm --add /dev/md1 /dev/sda2

Et observer la reconstruction  

    :::console
    cat /proc/mdstat

Bon hack !
