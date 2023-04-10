
Dies ist die README Datei für den Raspberry Pi Pico
---------------------------------------------------
Programmierung:

Welche Attribute gibt es:
 - self.raw  - Originale Wert
 - self.warn - Schwellwert für Warnung
 - self.alarm - Schwellwert für Alarm
 - self.vals  - Sinnvolle Auswahl an Werten

* Daten einlesen im Konstruktor ?

Welche Methoden bekommen die Klassen:
 - __init__(warn,alarm) - Constructor
   - warn               - Schwellwert Warning.
   - alarm              - Schwellwert Alarm.
 - read()      - liest Werte aus Hardware.
 - get()       - liefert den massgeblichen Wert zurück.
 - fhem()      - liefert einen FHEM String zurück.
 - html(clazz) - liefert HTML für Main Page.
   - clazz     - HTML class Angabe für <div> Element.
 - web()       - liefert HTML für Main Page, Werte und Graphik.
 - svg()       - liefert eine SVG zur Anzeige des massgeblichen Wertes.
 - debug()     - Optional zur Rückgabe von Datenstrukturen.
 - test()      - For test/run the code, instead of a separate test file.

---------------------------------------------------

Der Pico hat 2MB Flash Speicher.

Hardware
-----------
Der Kern des Raspberry Pi Pico und gleichzeitig das Alleinstellungsmerkmal im Vergleich zur Konkurrenz ist der von der Raspberry Pi Foundation selbst entwickelte Microcontroller RP2040. Kurz die wichtigsten Eckdaten:

    Dual-core Arm Cortex-M0+ mit bis zu 133MHz
    264 kB RAM
    2 MB interner Flash-Speicher
    8 programmierbare I/O State Machines (PIOs)
    30 GPIOs mit Mehrfachfunktion (am Pico sind 26 davon verfügbar), 
		davon 4 Analogeingänge (am Pico sind 3 davon verfügbar)
    USB 1.1 inkl. USB Mass-Storage-Unterstützung 
	(d.h., Geräte mit dem RP2040 können zur Programmierung wie ein USB-Stick genutzt werden)

Der RP2040 ermöglicht einen Zugriff auf bis zu 16MB externen Flash-Speicher (QSPI-Bus) und verfügt 
über einen DMA-Controller.

Über die 26 General Purpose Input/Output Pins (kurz GPIOs) können die folgenden Funktionen bzw. Bussysteme genutzt werden:

    3x Analog-Eingang (12 Bit Auflösung)
    16x PWM-Ausgang
    2x SPI-Bus (Serial Peripheral Interface)
    2x I2C-Bus (Inter-Integrated Circuit)
    2x UART (serielle Schnittstelle)


