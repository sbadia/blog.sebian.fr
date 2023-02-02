Title: Prosopopee ♥
Date: 2016-08-16 08:00
Author: Sebastien
About_author: Network and System engineer
Category: Asrall
Tags: photo, galery, python
Slug: prosopopee

Après avoir longtemps cherché la solution répondant à mes besoins en terme de
galerie photos, je crois que j'ai trouvé :)

## Solutions testées

* [ZenPhoto](http://www.zenphoto.org/), Plus en mode CMS, il y a une tonne de plugins, et d'intégration, nécessite une base de données.
* [Lychee](http://lychee.electerious.com/), alternative séduisante (graphiquement), assez actif niveau dev. mais pareil il faut une base de données, et la visu est en mode galerie.
* [Lazygal](http://sousmonlit.zincube.net/~niol/playa/oss/projects/lazygal/), bon là c'est statique, mais… il faut avoir des dons en CSS si on veut que ça ressemble à qqch :)

## Prosopopee

« More or less a small clone of exposure.co in form of a static generator. For those of you who don't know what exposure.co is, this allows you to tell a story with your pictures. »

* [prosopopee](http://prosopopee.readthedocs.org/en/latest/), C'est une galerie statique, mais qui permet de raconter une histoire, plus en mode fil, que simple galerie. J'adore!

J'ai d'ailleurs commencé à remplir mes pérégrinations…

* <http://peregrinations.sebian.fr/>

## Tips

Bon, une galerie photo, c'est cool, mais quid de la taille des photos et de l'aisance de visualisation (petite ligne ADSL…), la solution vient peut être avec le jpeg progressif !!

* <http://sebsauvage.net/rhaa/index.php?2013/07/30/14/35/17-grosses-images-et-petits-debits>
* <http://yuiblog.com/blog/2008/12/05/imageopt-4/>

Avec un petit script rapide :)

    :::bash
    #!/bin/sh
    file=$1
    set -ex
    # On optimse :)
    jpegtran -copy none -optimize "${file}" > "temp_${file}.jpg"
    rm -f "${file}"
    # Puis on passe l'encodage en "Progressive DCT, Huffman coding"
    jpegtran -copy none -progressive "temp_${file}.jpg" > "${file}"
    rm -f "temp_${file}.jpg"
    # Et enfin on vire les metadata (exif)
    mat "${file}"

Il reste donc plus qu'a écrire l'histoire :)
