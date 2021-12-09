# RCL
Unser Projekt ist eine Sprache, mit der man den Roboter kontrollieren kann. RCL steht für **Robot Control Language**. Das Projekt besteht, wenn man es im Ganzen sieht, 
aus einem Assembler geschrieben in Python und ein Interpreter geschrieben in C. Der Assembler liest den Code und assembled den Code zu einem String, 
der aus Zahlen besteht.
<br/>
<br/>
Die Zahlen können so aussehen:
  `{ 0.0, 255.0, 5.0, 1.0 }`
<br/>
Diesen String mit Zahlen kann man dann in den Assembler reinschieben und auf dem Roboter ausführen.

<br/>

> ***Was ist ein Assembler?*** Ein Assembler nimmt Befehle in Wortform und wandelt diese in Zahlen um, die der Computer verstehen kann

> ***Was ist ein Interpreter?*** Ein Interpreter führt die Befehle in Zahlenform aus


## Wie sind wir auf die Idee gekommen?
In den ersten Stunden haben wir uns überlegt, was wir überhaupt machen, doch uns war klar, dass wir **auf keinen Fall Scratch** benutzen würden. Wir haben ausprobiert, 
ob Python überhaupt funtioniert. Nein. Lösung: Eine eigene Sprache muss her.
So ist RCL entstanden. 

### Befehle
```
Bewegungsbefehle:
    forward     <speed> - roboter soll sich mit <speed> nach vorne bewegen
    backward    <speed> - roboter soll sich mit <speed> nach hinten bewegen 
    left        <speed> - roboter soll sich mit <speed> nach links bewegen
    right       <speed> - roboter soll sich mit <speed> nach rechts bewegen
    stop                - roboter soll anhalten

    jeder bewegungs-befehl überschreibt den vorherigen bewegungs-befehl

Programmflussbeeinflussung:
    wait <time>         - warte <time> sekunden lang
    exit                - Programm beenden

    point <point name> 				     - definiere einen Punkt mit dem namen <point name>
    jump <point name>				     - springe zu dem Punkt <point name>
    if <senor name> = <constValue> then <point name> - springe zu <point name> falls <sensorValue> das gleiche ist wie <constValue>
    if <senor name> > <constValue> then <point name> - springe zu <point name> falls <sensorValue> größer ist als <constValue>
    if <senor name> < <constValue> then <point name> - springe zu <point name> falls <sensorValue> kleiner ist als <constValue>

Speicher:
    <varname> = <value> - setze eine variable namens <varname> zu <value>

```

<br/>

```
point start

forward 100
wait 2
left 100
wait 0.5

jump start
```
*Dieser Code bewegt sich für 2 Sekunden nach vorne, 0.5 Sekunden nach links und wiederholt dies fortlaufend.*

## Welche Sensoren und Aktoren haben wir benutzt und wie funktioniert die Implementation
RCL hat die Kontrolle über zwei Sensoren, den LineFinding-Sensor und den Ultraschall-Sensor. Diese kann man mit einer Kondition ansprechen. ```if lineSensor = 0 then <aktion>```

# Entwicklung
## Struktogramme
```
Assembler                                                             Interpreter


 ┌─────┐                                                               ┌─────┐
 │Start│                                                               │Start│
 └──┬──┘                                                               └──┬──┘
    │                                                                     │
 ┌──▼────────────────────────────┐                                     ┌──▼──────────────────────────────┐
 │Datei mit Eingabeprogramm lesen│                                     │Liste an Befehlen als Zahle lesen│
 └──┬────────────────────────────┘                                     └──┬──────────────────────────────┘
    │                                                                     │
 ┌──▼───────────────────────────────┐                                  ┌──▼────────────────────────────┐
 │Nächsten Befehl von Programm laden◄───────────────┐                  │Nächsten Befehl von Liste laden◄────────────────────────────────────────────┐
 └──┬───────────────────────────────┘               │                  └──┬────────────────────────────┘                                            │
    │                                               │                     │                                                                         │
 ┌──▼─────────────────────────────────────────────┐ │                  ┌──▼─────────────┐             ┌────────────────┐                            │
 │Befehl plus angegebene Daten zu Zahlen umwandeln│ │                  │Befehl Kategorie├──Normal─────►Befehl ausführen├───────────────────────────►│
 └──┬─────────────────────────────────────────────┘ │                  │identifizieren  │             └────────────────┘                            │
    │                                               │                  │                │                                                           │
 ┌──▼──────────────────────────────────┐            │                  │                │             ┌─────────────────────────────────────────┐   │
 │Sind noch Befehle zum Übersetzten da?│            │                  │                ├──Jump───────►Befehl-Ausführung vor- oder zurückdrehen,│   │
 └──┬────────────────────────────────┬─┘            │                  │                │             │sodass der nächste Befehl richtig geladen├──►│
    │                                │              │                  │                │             │wird                                     │   │
   Nein                             Ja              │                  │                │             └─────────────────────────▲───────────────┘   │
    │                                │              │                  │                │                                       │                   │
 ┌──▼──────────────────────┐         │              │                  │                │             ┌───────────────────────┐ │                   │
 │Übersetzte Daten ausgeben│         └──────────────┘                  │                ├──Jump Cond──►Soll gesprungen werden?│ │                   │
 └──┬──────────────────────┘                                           │                │             └─┬───────────────────┬─┘ │                   │
    │                                                                  │                │               │ Nein           Ja │   │                   │
 ┌──▼─┐                                                                │                │               │                   └───┘                   │
 │Ende│                                                                │                │               │                                           │
 └────┘                                                                │                │               └──────────────────────────────────────────►┘
                                                                       │                │
                                                                       │                │             ┌────┐
                                                                       │                ├──Exit───────►Ende◄─┐
                                                                       │Spezial Fall:   │             └────┘ │
                                                                       │Ende der Liste  │                    │
                                                                       └─┬──────────────┘                    │
                                                                         │                                   │
                                                                         └───────────────────────────────────┘
```


## Tagebuch
***16.11***: Wir haben uns mit dem Projektaufbau vertraut gemacht und haben angefangen zu planen.

***18.11 + 19.11***: In diesen drei Stunden haben wir zuerst Ideen gesammelt und hatten wir einen groben Plan, wie unser Projekt aussehen wird. Danach haben wir versucht, die Python IDE zu starten und es hat leider nicht funktioniert. Nach vielen hoffnungslosen Versuchen haben wir uns entschlossen, ArduinoC zu benutzen, da wir keine andere Möglichkeit hatten außer Scratch und ArduinoC zu benutzen.

***23.11***: Langsam nimmt der Assembler und der Interpreter Form an und die ersten Befehle scheinen zu funktionieren. Doch schnell kommt das erste Problem und Debugging steht an.

***25.11 + 26.11***: Nach ein wenig Debugging funktioniert das erste Testprogramm und wir fingen an, an die Sensoren zu denken. Nach einem Konzept geht es wieder an die Arbeit doch es geht nicht voran. Fast nichts scheint zu funktionieren, Sensoren geben nichts zurück, Motoren machen nichts, usw.

***30.11***: Probleme über Probleme, nichts scheint zu funktionieren. Verzweifelt versuchen wir wenigstens die einfachsten Testprogramme zum Laufen zu bekommen.

***02.12 + 03.12***: Es scheint wieder zu funktionieren und wir arbeiten an einfachen Bugs in unserer Software. Während Simon weiter an Fehlern arbeitet, fängt Niklas an mit der Dokumentation.

***07.12***: Niklas arbeitet weiter an der Dokumentation, während Simon an dem LineFinder weiterarbeitet, was scheinbar nicht funktioniert. 

