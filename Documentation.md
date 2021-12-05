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



# Entwicklung
## Struktogramme
*insert structograms her*
## Tagebuch
