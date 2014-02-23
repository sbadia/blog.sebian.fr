Title: Vim SnipMate
Date: 2011-04-29 08:23
Author: Sebastien Badia
About_author: Sys/Net admin engineer @Inria, LDN Co-founder.
Category: Tips
Tags: snippet, vim
Slug: vim-snipmate
Modified: 2014-02-23 17:07

Les utilisateurs de mac connaissent sans doute [Textmate](http://macromate.com/), un editeur de texte avec des fonctionnalités vraiment sympa, au niveau coloration, langage, et j'en passe, bon j'arrête d'en faire la promotion, car j'ai récemment découvert un plugin [vim](http://www.vim.org/) qui fait la même chose :D

Les [Snipmate](http://www.vim.org/scripts/script.php?script_id=2540) gèrent une quantité de langages, mais rien ne vous empêche d'écrire votre snippet.

Par exemple un snippet pour compléter un header automatiquement

    :::vim
    snippet #header
            # Author:: `system("git config user.name")` (<`system("git config user.email")`>)
            # Date:: `system("ruby -e 'puts Time.now'")`

Hop je tape *#header* suivi d'une tabulation, et je me retrouve avec ça :)

    :::console
    # Author:: Sebastien Badia (‹seb@mail.fr›)
    # Date:: Fri Apr 29 08:19:08 +0200 2011

[Snipmate on github](https://github.com/msanders/snipmate.vim)
