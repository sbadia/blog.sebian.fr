Title: Map Vim
Date: 2010-02-14 14:10
Author: Sebastien
About_author: ASRALL Student
Category: Tips
Tags: Debian, Tips
Slug: map-vim
Modified: 2014-02-23 17:07

## Petites macro dans vim

Pour enregistrer un document latex et le compiler directement !

    :::vim
    :map <F10> :w <CR> :! pdflatex % <CR><CR>

Pour le visualiser dans evince !

    :::vim
    :map <F11> :evince % <.pdf @ <CR><CR>

Vous l'aurrez compris on appuye sur F10 pour compiler et enregistrer et sur F11 pour le visualiser dans evince.
