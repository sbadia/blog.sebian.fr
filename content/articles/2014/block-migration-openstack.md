Title: OpenStack block migration
Date: 2014-08-06 04:14
Author: Sebastien Badia
About_author: Engineer @eNovance, Puppet addict and Net Neutrality defender.
Category: Tips
Tags: OpenStack, Nova, Libvirt, Qemu
Slug: openstack-block-migration

## Contexte

Niveau contexte, la plateforme en place n'utilise pas de shared-storage, mais les images sont au format qcow2 avec un `backing_file` ce qui permet d'avoir une image bien sparsé.

Lors d'une migration via nova/libvirt en mode block le comportement observé est un merge de l'image transférée + du `backing_file` + reste de l'image en mode raw (si on a une image non sparsé de 20Go, alors 20Go de zéro transitent sur le réseau, l'image n'est pas re-sparsifié de l'autre coté), mais la migration fonctionne.

## Analyse

Les flags de [live-migration](https://github.com/openstack/nova/blob/14080812961e5a2f6a7054a45d2afa013e4f3899/nova/virt/libvirt/driver.py#L169-L170) par défaut dans nova icehouse (version 2014.1-2~bpo2012.04+1) sont `VIR_MIGRATE_UNDEFINE_SOURCE, VIR_MIGRATE_PEER2PEER` donc pas de « vraie » live-migration. Nova dispose de [flags différents](https://github.com/openstack/nova/blob/14080812961e5a2f6a7054a45d2afa013e4f3899/nova/virt/libvirt/driver.py#L4493-L4495) pour la migration en [mode block](https://github.com/openstack/nova/blob/14080812961e5a2f6a7054a45d2afa013e4f3899/nova/virt/libvirt/driver.py#L172-L174) les defaults étant `VIR_MIGRATE_UNDEFINE_SOURCE, VIR_MIGRATE_PEER2PEER, VIR_MIGRATE_NON_SHARED_INC`

Le cycle de live migration en mode block fait appel directement à libvirt à travers la méthode [migrateToURI](https://github.com/openstack/nova/blob/14080812961e5a2f6a7054a45d2afa013e4f3899/nova/virt/libvirt/driver.py#L4500-L4503) (ce qui est corroboré avec un simple lsof sur le disk qcow2 de destination/départ lors de la migration).

Au niveau des flags libvirt intéressant (dans le code actuel) il y a le `VIR_DOMAIN_BLOCK_REBASE_REUSE_EXT`, cf la ML libvirt [archives2012](http://www.redhat.com/archives/libvir-list/2012-April/msg00292.html)

    :::console
    « Management applications can pre-create the copy with a relative backing file name, and use the VIR_DOMAIN_BLOCK_REBASE_REUSE_EXT flag to have qemu reuse the metadata; if the management application also copies the backing files to a new location, this can be used to perform live storage migration of an entire backing chain. »

Mais même comportement, avec une combinaison de `VIR_DOMAIN_BLOCK_REBASE_COPY|VIR_DOMAIN_BLOCK_REBASE_SHALLOW` en gardant en mémoire de s'assurer que le `backing_file` était présent sur les différents computes (ce qui n'est pas le cas lorsque aucune image du même « type » n'a été booté sur le compute…), cette combinaison fonctionne (sans non-shared storage incrémental (`VIR_MIGRATE_NON_SHARED_INC`)).

Nova dispose d'une boucle de code pour synchroniser/vérifier que les rbase sont présent sur les compute, nous faisons donc le test d'évacuer un compute, booter une vm sur le deuxième et avant la migration, de supprimer les rbase (backing) et enfin de lancer la migration. Résultat tout se passe comme convenu, nova transfère le rbase correspondant avant la migration.

## Tests

    :::console
    block_migration_flag=VIR_MIGRATE_UNDEFINE_SOURCE,VIR_MIGRATE_PEER2PEER,VIR_MIGRATE_LIVE,VIR_DOMAIN_BLOCK_REBASE_COPY,VIR_DOMAIN_BLOCK_REBASE_SHALLOW

Nova boot en précisant le compute (histoire de pouvoir tuer le rbase) (`--availability_zone nova:compute-01`)
verif du qcow2.

    :::console
    qemu-img info /var/lib/nova/instances/<id>/disk

Identification du `backing_file` et remove sur la dest

    :::console
    mv /var/lib/nova/instances/_base/c99ee4f8dc122039d37be31ef5064345acf886be{,.back}

Puis migration:

    :::console
    nova live-migration --block-migrate myvm

Verifications du qcow2 et du backing (il est recré), donc pas d'effets de bord de la suppression du flag INC, et pas de soucis si le rbase est pas présent.

## Littérature / pointeurs

* [Super doc d'Ovirt à propos des contextes/migrations](http://www.ovirt.org/Features/Design/StorageLiveMigration)
* [Bug posé à l'origine sur nova](https://bugs.launchpad.net/nova/+bug/1350857)
* [Migration en mode blocopy](http://kashyapc.com/2014/07/06/live-disk-migration-with-libvirt-blockcopy/)
* [Et w/o shared](http://hgj.hu/live-migrating-a-virtual-machine-with-libvirt-without-a-shared-storage/)
* [Quelques flags intéressants](http://www.redhat.com/archives/libvir-list/2012-April/msg00292.html)
* [Optims de sync pour les rbases](https://review.openstack.org/#/c/9944/)
* [Différences p2p/tun](http://libvirt.org/migration.html)
