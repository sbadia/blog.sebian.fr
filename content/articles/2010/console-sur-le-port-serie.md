Title: Console sur le port série
Date: 2010-03-11 15:35
Author: Sebastien
About_author: ASRALL Student
Category: Tips
Tags: console, tty, serie, switchs
Slug: console-sur-le-port-serie
Modified: 2014-02-23 17:07

## États des lieux

Aujourd'hui la plus-part des Switch avec interface de management sont doté d' une interface de configuration Web,  mais ce n'est pas le cas de tous. Ou tout simplement pour des soucis de sécurité, le port console est une très bonne solution.

Bien sûr la seul alternative pour se connecter en série sur le port console n'est pas un bon vieux pc sous Win2k avec indispensable Hyper-Terminal, oui oui c'est bon vous pouvez le mettre au placard!

La solution sur Debian et autres systèmes GNU-Linux c'est Minicom.

## Avant la bataille

On commence par regarder si le port série de sa machine est bien reconnu ;)

    :::console
    dmesg | grep Serial | head -1 && dmesg | grep ttyS0

Devrais renvoyer ceci:

    :::console
    [    1.151414] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
    [    1.151527] serial8250: ttyS0 at I/O 0x3f8 (irq = 4) is a 16550A
    [    1.151938] 00:08: ttyS0 at I/O 0x3f8 (irq = 4) is a 16550A

Tout est donc géré par le 16550A.

Regardons les droits maintenant, normalement ils sont bons mais vérifions ;)

    :::console
    ls -l /dev/ttyS0

Nous retourne

    :::console
    crw-rw---- 1 root dialout 4, 64 11 mars  14:29 /dev/ttyS0

On peux alors regarder si notre utilisateur est dans le groupe "dialout", si ce n'est pas le cas on peux l'ajouter avec un

    :::console
    adduser tutu dialout

## C'est parti

On peux maintenant attaquer le coeur du problème ! Oui il était temps ;)

    :::console
    apt-get install minicom

Le paquet "lrzsz" est en dépendance. Un petit coup de man peut être utile...

    :::console
    minicom -s

Pour la configuration de minicom.

    :::console
    +------------[configuration]-----------+
    | Noms de fichers et chemins           |
    | Protocoles de transfert              |
    | Configuration du port série          |
    | Modem et appel                       |
    | Ecran et clavier                     |
    | Enregistrer config. sous dfl         |
    | Enregistrer la configuration sous... |
    | Sortir                               |
    | Sortir de Minicom                    |
    +--------------------------------------+

On peux se promener dans les menus puis aller dans "configuration du port série". Puis on appuye sur la lettre "A" pour changer le chemin et la parité.

* Port série : /dev/ttyS0
* Débit/Parité/Bits : 9600 8N1

Une fois tous les réglages effectués on enregistre la config avec "Enregistrer config. sous dfl" Et on sélectionne "Sortir" pour lancer le programme. Et voila nous voila sur l'interface de notre chère switch ;)

On redémarre ensuite le switch pour voir passer sa configuration...

![baystack-self]({static}/images/baystack-Self.png)

Et voila maintenant le superbe menu du Baystack 350T.

![baystack-menu]({static}/images/baystack-Menu.png)
