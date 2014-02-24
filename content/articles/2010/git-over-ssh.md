Title: Git over Ssh
Date: 2010-10-23 12:07
Author: Sebastien Badia
About_author: ASRALL Student
Category: Tips
Tags: git, ssh
Slug: git-over-ssh
Modified: 2014-02-23 17:07

Sur le client et sur le serveur, exécuter la commande suivante.

    :::console
    apt-get install git git-core

Modifications d'usage pour les logs...

    :::console
    git config --global user.email "yourmail@example.com"
    git config --global user.name "Your Name"

Sur le client on crée le repo.

    :::console
    mkdir projet cd projet git init
    #Initialized empty Git repository in .git/

On ajoute maintenant un fichier à notre repo.

    :::console
    echo "Hello World" > README
    git add . git commit -m "First Commit"
    > Created initial commit c491bd6: First Commit
    > 1 files changed, 1 insertions(+), 0 deletions(-)
    > create mode 100644 README

Puis on clone le repo et on utilise l'option bare pour construire les objets.

    :::console
    cd ..
    git clone --bare project projet.git
    > Initialized empty Git repository in /path/to/projet.git/
    > 0 blocks
    ls projet.git
    > branches  config  description  HEAD  hooks  info  objects  refs

Enfin on copie le récent clone sur notre serveur.

    :::console
    scp -r projet.git toto:~/git

> Toto est un host bien configuré dans le fichier .ssh/config

Et voila tout est bien configuré ! Il ne nous reste plus qu'a cloner le dépot où on le souhaite.

    :::console
    git clone toto:git/projet.git
