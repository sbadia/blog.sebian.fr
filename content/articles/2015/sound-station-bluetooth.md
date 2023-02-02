Title: Enceinte portable bluetooth et pulseaudio
Date: 2015-08-26 07:00
Author: Sebastien
About_author: Engineer @RedHat, Puppet addict and Net Neutrality defender.
Category: Asrall
Slug: enceinte-bluetooth

Le but de ce billet est de configurer une enceinte portable bluetooth avec un
ordinateur aussi équipé de ce protocole.

## Avance de commencer

Avance de commencer, assumons que :

* Ma machine est équipé d'un contrôleur bluetooth
* Que je dispose d'une enceinte bluetooth (ah? ça ne fonctionne pas sans? euh… :-D)
* La MAC address de l'enceinte est *aa:bb:cc:dd::ee:ff*

Bien sûr ces « variables » ne seront pas les mêmes dans votre cas.

## À l'attaque!

On commence par vérifier que le service est bien lancé, et que le bluetooth
n'est pas désactivé de façon logicielle. (c'est mon cas, donc je le réactive).

    :::bash
    sudo systemctl status bluetooth.service
    sudo rfkill list
    sudo rfkill unblock bluetooth

Le reste se passe via le pseudo-shell bluetooth, que nous lançons via la
commande:

    :::bash
    bluetoothctl

Le prompt change alors pour nous indiquer que nous sommes bien dans un autre
environnent, nous allons donc activer le module (normalement c'est déjà ok, mais
pas grave), puis lancer un agent, et demander un scan des périphériques à porté
de bluetooth.

    :::bash
    [bluetooth]# power on
    [bluetooth]# agent on
    [bluetooth]# scan on

À ce stade, le scan précédent devrait afficher une ou des nouvelles adresses
MAC dans le terminal.

    :::bash
    [NEW] Device aa:bb:cc:dd::ee:ff JBL Charge

Il suffit donc de sélectionner la MAC de l'enceinte désiré, et de s'y connecter
(pair, trust puis connect).

    :::bash
    [bluetooth]# pair aa:bb:cc:dd::ee:ff
    [bluetooth]# trust aa:bb:cc:dd::ee:ff
    [bluetooth]# connect aa:bb:cc:dd::ee:ff

Et voila! On peut maintenant fermer le pseudo-shell bluetooth.

    :::bash
    [bluetooth]# quit

Il ne reste donc plus qu'à aller dans les réglages de pulseaudio, ou via
*pavucontrol* et de sélectionner l'enceinte comme sortie de son.

## Notes

Il est probablement possible que pulseaudio râle un peu, pas de panique en
principe tout rentre dans l'ordre en le relançant, pour cela il suffit
d'exécuter ces commandes :

    :::bash
    pulseaudio -k
    pulseaudio -D

## Conclusion

Have fun avec votre super nouvelle enceinte !

## Edit (2016-04-02)

Hum, j'ai rencontré quelques soucis, notamment l'enceinte qui est pairé mais
jamais vue en sink dans pulseaudio.

Visiblement ça serait à cause de blueman, mais je n'ai pas vérifié.

    :::bash
    pactl load-module module-bluetooth-discover
    pactl load-module module-switch-on-connect
    # Votre enceinte devrait apparaitre :)
    pactl list sinks short

### Sources

* <https://unix.stackexchange.com/a/159882>
* <https://wiki.archlinux.org/index.php/PulseAudio/Troubleshooting>

## Edit (2016-05-25)

### Sources

Bon, suite à une mise à jour, plus rien ne fonctionnait, mais la solution est
encore dans le wiki Archilinux (à croire que…).

    :::bash
    # /etc/bluetooth/audio.conf
    [General]
    Enable=Socket

* <https://wiki.archlinux.org/index.php/Bluetooth_headset#Audio_sink_fails>
