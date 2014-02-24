Title: Script pub !
Date: 2010-12-14 14:51
Author: Sebastien Badia
About_author: ASRALL Student
Category: Tips
Tags: pub, script, Tips
Slug: script-pub
Modified: 2014-02-23 17:07

Certains utilisent pastebin, ou autre pour partager rapidement un bout de code ou autre, mais avec un fichier binaire ? Ou bien pour tout simplement maîtriser ce que vous publiez?

La réponse est chez [madduck](http://madduck.net/blog/2007.01.12:featured-tool--pub/), c'est un petit script bash pour publier rapidement n'importe quel type de fichier.

Le script utilise *scp* et *liburi-perl*, pour une utilisation simplifié copier le script dans votre PATH (/usr/local/bin) pour moi.

Créer un fichier *~/.pubrc*

    :::bash
    # ~/.pubrc
    TARGETHOST="sebianw"
    TARGETDIR="/var/www/pub/"
    PUBBASE="http://sebian.yasaw.net/pub/"

> sebianw est un host bien configuré dans mon *~/.ssh/config*

Sécurisez un peu votre dossier (sur votre serveur web).

    :::apache
    ‹Directory /var/www/pub/›
      Options -Indexes
      Order allow,deny
      Allow from all
    ‹/Directory›

Et c'est parti !

    :::console
    pub /usr/local/bin/pub
    > http://sebian.yasaw.net/pub/pub size:11366 hash:9890b44152dba310d98d339acc7b0aea

Le script en question est ici [http://sebian.yasaw.net/pub/pub](http://sebian.yasaw.net/pub/pub), n'hesitez pas à regarder les options (doc dans le script).

Merci à [Lucas](http://www.lucas-nussbaum.net/) pour sa découverte/utilisation/transmission !
