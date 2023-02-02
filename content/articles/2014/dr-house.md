Title: Diagnostiquer tel un Dr.House
Date: 2014-08-24 15:11
Author: Sebastien
About_author: Engineer @eNovance, Puppet addict and Net Neutrality defender.
Category: Asrall
Tags: Diagnostic, Informatique, Debug
Slug: dr-house-adminsys

Une des principales tâches d'un admin sys/net réside dans la capacité à diagnostiquer et surtout à résoudre des problèmes.

Cela n'est bien entendu pas spécifique à l'informatique (voir [medical diagnosis](http://en.wikipedia.org/wiki/Medical_diagnosis)).

![linuxobservabilitytools](//blog.sebian.fr/images/linux_observability_tools.png)

Les outils permettant d'arriver à une solution et la/les méthode(s) de résolution sont souvent les mêmes, ils passent par :

* La connaissance technique
* L'expérience de l'admin
* La méthodologie

Voici donc quelques pointeurs pour vous faciliter la vie!

# Sources / Lecture

Cette liste est bien entendu non exhaustive, mais c'est un bon début.

## [James Golick](http://jamesgolick.com/)

Des slides de James Golick [how-to-debug-anything](http://en.slideshare.net/jamesgolick/how-to-debug-anything), l'aspect méthodologie est plus mis en avant. La conférence est axée sur la résolution d'un problème particulier et le découpage en étapes.

## [Lucas Nussbaum](http://www.loria.fr/~lnussbau/)

Des slides complets de Lucas, en Licence Pro. [ASRALL](http://asrall.fr/), Intitulés [asrall-s-problemes](http://www.loria.fr/~lnussbau/files/asrall-s-problemes.pdf) la conférence/cours aborde tous les aspects de l'art du diagnostique informatique.

## [Brendan Gregg](http://www.brendangregg.com/)

Et enfin, le meilleur pour la fin :-)

Brendan Gregg ([photo](http://www.brendangregg.com/blog/images/2014/brendan_linuxconna2014.jpg)) est une référence dans le domaine, il est l'auteur du livre « Systems Performance: Enterprise and the Cloud » [voir](http://www.brendangregg.com/sysperfbook.html) sysperfbook.

La page [linuxperf](http://www.brendangregg.com/linuxperf.html) est juste une merveille, et les schémas sont bien représentatifs:

* [Outils pour le debug](http://www.brendangregg.com/Perf/linux_observability_tools.png)
* [Page dédiée à sar](http://www.brendangregg.com/Perf/linux_observability_sar.png)
* [Pour les benchs](http://www.brendangregg.com/Perf/linux_benchmarking_tools.png)
* [Et le tunning](http://www.brendangregg.com/Perf/linux_tuning_tools.png)

Have fun!
