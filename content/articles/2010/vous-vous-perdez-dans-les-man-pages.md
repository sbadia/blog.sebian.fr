Title: Vous vous perdez dans les man-pages?
Date: 2010-02-14 14:26
Author: Sebastien
About_author: ASRALL Student
Category: Tips
Tags: Tips
Slug: vous-vous-perdez-dans-les-man-pages
Modified: 2014-02-23 17:07

Merci pour la petite astuce de Mr Vallar, et par la même occasion à [Luc](http://lucdidry.free.fr/).

Voila une petite astuce bien utile, elle s'appelle "most" , comme less, ou more, elle affiche ce qu'on lui passe en paramètre, mais... on peux dire que c'est un less/more boosté aux stéroids...

On peux donc utiliser cette commande pour lire les man, et c'est bien pratique, car le texte en gras sera coloré

    :::console
    apt-get install most

Et pour l'utiliser dans le man il suffit de changer les alternatives.

    :::console
    update-alternatives --config pager`

Bon man !!
