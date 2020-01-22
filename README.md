# Project_Pi
**GKNB_INTM020 Mikroelektromechanikai rendszerek**

## Szükséges Eszközök:
- Raspberry PI model 4 B
- PIR mozgásérzékelő szenzor + 3db Anya-Anya jumper kábel(jár hozzá)
- Raspberry Pi Camera modul v2
- Micro SD kártya, minimum 8GB
- Micro HDMI - HDMI kábel vagy Micro HDMI - HDMI átalakító és HDMI-HDMI kábel
- Billentyűzet + egér + monitor
- USB-C típusú tápkábel

## Rakjuk össze az eszközt:

Az építésnél mindenképp figyeljünk arra, hogy az áramot utoljára csatlakoztassuk az eszközre, hogy mindenképpen elkerüljük az áramütést.
Figyeljünk arra, hogy a telepítéshez kizárólag vezetékes egér és billentyűzet használható, viszont a telepítés után bátran csatlakoztathatunk vezeték nélküli megoldást is.


## Első lépések

### Frissítsük a Pi-t, az alábbi kódokkal:
- sudo apt-get update
- sudo apt-get upgrade
- sudo pip install gpiozero
- sudo pip install matplotlib
- sudo pip install
- sudo apt-get install ssmtp mailutils --email
