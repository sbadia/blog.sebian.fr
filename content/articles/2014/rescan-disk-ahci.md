Title: Rescan bus ahci/sata & disques « hot-swap »
Date: 2014-08-08 12:05
Author: Sebastien
About_author: Engineer @eNovance, Puppet addict and Net Neutrality defender.
Category: Asrall
Tags: Ahci, Sata, HotSwap, HDD
Slug: rescan-ahci

Sur nos serveurs et même pc récents les cartes supportent le « hot-swap » càd ajouter et retirer des disques à chaud (quand la machine est allumée), mais il arrive parfois que le système n'arrive pas à s'interfacer complètement avec le nouveau disque. Dans notre cas (sur l'infra de [LDN](http://ldn-fai.net/)), un reboot était exclu (ce que j'aurais sans doute fait si j'avais eu ce problème sur mon ordinateur personnel).

# Problème

On vient donc d'ajouter le nouveau disque à chaud, celui-ci est bien reconnu, on le voit dans un `dmesg` et un `hdparm -I` nous donne ses infos. On crée donc deux partitions dessus, pour la première pas de soucis, cependant pour la seconde ça coince… On lance donc un rescan.

    :::bash
    # partprobe /dev/sda
    Error: Error informing the kernel about modifications to partition /dev/sda2 --
    Device or resource busy.
    This means Linux won't know about any changes you made to /dev/sda2 until you reboot -- so you shouldn't mount it or use it in any way before rebooting.
    Error: Failed to add partition 2 (Device or resource busy)

Le système lui-même nous demande de redémarrer :-) (dans le genre « achevez moi, svp, bisous »)

    :::bash
    # kpartx -l /dev/sda
    sda1 : 0 1953523120 /dev/sda 2048
    sda2 : 0 1953504000 /dev/sda 1953525168

Mais nous ne lui laisserons pas ce plaisir, on tente donc directement dans `/sys` en mode barbu.

    :::bash
    # echo 1 > /sys/block/sda/device/rescan
    # partx -l /dev/sda
    1:      2048-1953525167 (1953523120 sectors, 1000203 MB)
    2: 1953525168-3907029167 (1953504000 sectors, 1000194 MB)
    # partx -a -v /dev/sda
    partition: none, disk: /dev/sda, lower: 0, upper: 0
    /dev/sda: partition table type 'dos' detected
    partx: /dev/sda: adding partition #1 failed: Device or resource busy
    partx: /dev/sda: adding partition #2 failed: Device or resource busy
    partx: /dev/sda: error adding partitions 1-2
    # ls /dev/sda*
    /dev/sda  /dev/sda1

Mais sans succès non plus, impossible de rescan correctement le disque…

Nous avons donc testé les méthodes classiques à base de :

* `partprobe`:
* `partx` / `kpartx`:
* `echo` dans `device/rescan`:
* <s>reboot</s>

# Résolution

Ok, donc si on résume, disque : 1, nous : 0 … On emploie donc les les grands moyens !

Suppression du disque (oui carrément, et non ce n'est pas pour toujours.)

    :::bash
    # echo 1 > /sys/block/sda/device/delete

Et enfin on force le re-scan via le `scsi_host`

    :::bash
    # echo "- - -" >/sys/class/scsi_host/host0/scan

`host0` correspond à l'id du bus où le disque est connecté (pensez à regarder avant de faire le delete :p)

# Liens / Sources

* Un lien serverfault sur le [rescan hot-swap](http://serverfault.com/questions/5336/how-do-i-make-linux-recognize-a-new-sata-dev-sda-drive-i-hot-swapped-in-without)
* Une bonne doc sur unixadminschool sur le [scsi-hot-swap](http://unixadminschool.com/blog/2011/05/linux-dynamically-addremove-scsi-from-linux/)
* Ou le thread initial sur la mailing liste de [Lorraine Data Network](http://listes.ldn-fai.net/pipermail/benevoles/2014-August/001855.html)

_Note_: Aucun disque n'est mort durant ce post :-)


Un grand **Merci** à Jonathan pour l'aide ;-)
