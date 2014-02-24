Title: Tunnel Ssh
Date: 2010-08-16 23:36
Author: Sebastien Badia
About_author: ASRALL Student
Category: Tips
Tags: Réseau, Ssh, Tips
Slug: tunnel-ssh
Modified: 2014-02-23 17:07

Il ne vous est jamais arrivé d'être loin de chez vous et de vouloir accéder à l'interface de votre box (chez vous) depuis votre serveur qui est derrière cette dernière?

J'ai nommé les tunnels Ssh, vraiment super pratique, cela permet d'en-capsuler tout le flux web (dans notre cas) dans le tunnel, et ainsi d'accéder à une ressource inaccessible de l'extérieur...

Le Tunnel à proprement dit.

    :::console
    ssh -L 3443:machinbox:80 gnu

On ouvre ici le tunnel en local sur le port 3443 (au dessus de 1000 car réservé avant) sur le port 80 de la machinbox depuis notre serveur gnu (correctement configuré seb@gnu.sebian.fr)

Enfin avec un navigateur on utilise le tunnel tout simplement en se connectant à

* http://localhost:3443
