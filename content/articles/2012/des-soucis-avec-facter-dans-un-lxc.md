Title: Des soucis avec facter dans un lxc ?
Date: 2012-10-28 15:17
Author: Sebastien
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: debian, facter, lxc, puppet
Slug: des-soucis-avec-facter-dans-un-lxc
Modified: 2014-02-23 17:07

Depuis quelques versions de facter (l'outil que puppet utilise pour récupérer les infos du système hôte), je rencontrais un soucis étrange avec selinux.

Mais je n'avais pas de selinux activé… et je suis assez à jour.

    :::console
    facter -v 1.6.13

Le soucis en question a fait l'objet d'un [bug](http://projects.puppetlabs.com/issues/4466) chez puppetlabs.

    :::console
    facter -y
    > Could not retrieve selinux: Invalid argument - /proc/self/attr/current
    > kernel: Linux

Pour «corriger» ce soucis il suffit de supprimer le fichier */selinux/enforce* (à 0 dans mon cas)

    :::console
    rm -f/selinux/enforce

Ou part puppet lui même !

    :::puppet
    file { '/selinux/enforce': ensure => absent; }

Et voila, vous pouvez enlever «**> /dev/null 2>&1 || true**» de vos cron ;)

Source: Merci à [Mattias Geniar](http://mattiasgeniar.be/2012/07/31/facterpuppet-could-not-retrieve-selinux-invalid-argument-procselfattrcurrent/) pour le tips.
