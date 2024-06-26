# Station-F
## Casus
In nederland hebben we een spoorwegennetwerk dat stations met elkaar verbindt. Hierdoor kom je bijvoorbeeld van Utrecht naar Amsterdam. Echter, niet alle stations hebben een verbinding met elkaar. Zo kom je alleen via Alkmaar bij Den Helder. De NS wil een zo goed mogelijk spoorwegennetwerk en het is een uitdaging om daarvoor een goede dienstregeling te maken. Om te voldoen aan een correcte dienstregeling voor heel Nederland mogen er maximaal 20 trajecten gebruikt worden, die elk maximaal 180 minuten duurt. De dienstregeling wordt beter wanneer meer verbindingen worden bereden, minder trajecten en minder minuten worden gebruikt. Om dit probleem op te lossen, worden algoritmen gebruikt. Om te bepalen hoe goed een lijnvoering is, is er een kostenfunctie (K) die we willen maximaliseren.
De volgende aspecten hebben invloed op de score: 

K = kwaliteit van de dienstregeling  
p = fractie gereden verbindingen ten opzichte van het totaal aan mogelijke verbindingen  
T = Het aantal trajecten in de dienstregeling  
Min = het totaal aantal gereden minuten   
```
  K = p*10000 - (T*100 + Min)
```

Om het probleem op een kleinere schaal te kunnen weergeven, is er ook een kaart van alleen Noord- en Zuid-Holland beschikbaar.

## State Space
##### NEDERLAND  
  
De state space van heel Nederland is berekend aan de hand van de volgende aannames:
* Er worden 36 verbindingen per traject gereden, want:
  * Een traject heeft maximaal 180 minuten
  * De kortste verbinding duurt 5 minuten
* Bij elk station heb je 9 opties, want
  * Utrecht Centraal heeft als meeste 9 opties (N=9)
* In totaal worden er maximaal 20 trajecten gevormd, maar omdat het ook mogelijk is om een verschillend aantal trajecten te hebben voor een oplossing, moeten al deze opties meegenomen worden in het berekenen van de state space.

**Eén traject**  
Volgorde is belangrijk  
Herhaling kan  
-> $ n^r $, waarbij n=9 en r=36
```
9^36 = 2.25 * 10^34
```
Dit resultaat wordt vervolgens gebruikt om de state space van de hele dienstregeling te bepalen.

**Hele dienstregeling**  
Volgorde is niet belangrijk  
Herhaling kan  
-> $(r+n-1)! \over (r!(n-1)!) $, waarbij n=2.25*10^34 en r=20

Formule voor de trajecten waarbij repetitie kan en volgorde is belangrijk: 
N^r 
9^36 = 2.25 * 10^34

Formule voor de hele dienstregeling waarbij repetitie kan en volgorde niet belangrijk is
(r+N-1)!/r!(N-1)!
N = 9^36
r = 20
```
(20+9^36-1)!/20!(9^36-1)! = undefined
```
Dit resultaat is te groot voor een rekenmachine om uit te rekenen. 

## Algoritmes
### Random 
Voor de baseline is een random algoritme gebruikt. Hierbij worden de volle minuten gebruikt per traject, is het mogelijk om verbingen dubbel te rijden en is het aantal trajecten random en worden verbindingen random gekozen. Deze baseline is verder uitgewerkt met een aantal experimenten, om een gevoel te krijgen voor de invloed van bepaalde parameters op de scores.

**Experimenten**  
In een van de experimenten wordt in plaats van een random aantal trajecten, het maximale aantal trajecten gebruikt.   
In een ander experiment worden verbindingen niet dubbel bereden, tenzij het niet anders kan. Hierbij wordt weer een onderscheid gemaakt tussen enerzijds een random aantal trajecten, anderzijds het maximale aantal trajecten.  
Als laatste hebben we ook nog gekeken naar de invloed van het gekozen startstation, waarbij er bij het aanmaken van een traject een station wordt gekozen dat nog niet eerder is bereikt.

Om het optimale aantal trajecten te hanteren, hebben we een experiment gedaan. Het theoretisch minimale aantal trajecten is voor heel Nederland 9. Dus, de random en de slimmere random algoritmes zijn uitgevoerd voor elk aantal trajecten van 9 t/m 20. Hieruit bleek dat met 13 trajecten de random algoritmes de beste resultaten konden verkrijgen.  

### Greedy
Om een beeld te krijgen van hoe zo'n dienstregeling wordt opgebouwd, is een constructief algoritme gebruikt; de greedy. 
De algemene (domme) greedy is gebaseerd op de volgende aannames:
* een vast aantal trajecten
* een random start station
* de kortste connectie wordt elke keer gekozen, mits deze nog niet gereden is
* trajecten worden maximaal gevuld, of tot er geen verbindingen meer mogelijk zijn

**Experimenten**  
Om de greedy slimmer te maken is de Smart Greedy ontstaan, die afwijkt wat betreft start station: voor het start station wordt het station met de minste verbindingen gekozen uit een lijst van stations dat nog onbereden verbindingen heeft  
Ook is er een random greedy gemaakt, waarbij er op basis van kansen de langste, kortste of random verbinding wordt gekozen.


Ook bij de greedy is er onderzoek gedaan naar het optimale aantal trajecten. Bij de domme greedy was dit 19, en bij de smart greedy was het 17.

### Hill Climber
Als laatste een iteratief algoritme: de HillClimber.  
Als basis hebben we een simpele hillclimber gemaakt die start met een random dienstregeling en vervolgens random 1 traject verwijdert en random een nieuw traject aanmaakt.  
Elke hillclimber begint met een random dienstregeling.  

Op basis hiervan zijn we gaan experimenteren om de hillclimber te verbeteren

**Experimenten**  
Als eerste hebben we experimenten gedaan met het verwijderen en toevoegen van trajecten. Zoals bijvoorbeeld 4 verwijderen en 2 toevoegen. Dit liet geen verbeteringen zien, dus blijft de rest van de hillclimbers 1 traject verwijderen en 1 traject toevoegen.  
In een ander experiment mogen nieuwe trajecten geen dubbel bereden verbindingen hebben.  
Nog een experiment onderzoekt de smart start station heuristiek, die bij de greedy en de random ook is toegepast. Hierbij zagen we tijdens het plotten dat stations aan de zijkanten langs het traject werden overgeslagen. Hieruit volgde het laatste experiment:  
Een hillclimber waarbij trajecten slim worden verwijderd: alleen trajecten die langs een onbereden verbinding liggen worden verwijderd en weer opnieuw gelegd.  

Ook bij de hillclimber hebben we onderzocht wat het optimale aantal trajecten is. We hebben dit aan de hand van de basis hillclimber (1 weg 1 erbij) en de smart start hillclimber gedaan. Hier kwam uit dat 11 trajecten het optimale aantal trajecten is.

Voor het uitvoeren van bovenstaande experimenten gebruiken we daarom 11 als vast aantal trajecten. 


## Instructies

### Vereisten
Deze code is geschreven in python3. Installeer alle benodigde pakketten dmv:
```
$ pip install -r requirements.txt 
```
### Gebruik
Om de experimenten te runnen worden command line arguments gebruikt. Deze experimenten zijn al voorgemaakt, op basis van bepaalde iteraties en heuristieken. Het is dus alleen mogelijk om via de command line de vaste experimenten te runnen.  
  
De standaardvorm ziet er als volgt uit:
```
$ python3 main.py -k [kaart] -a [algoritme] -ex [experiment]
```
waarbij:  
-k / --kaart: de kaart die je wilt gebruiken. opties: nl, nh  
-a / --algoritme: het algoritme dat je wilt runnen. opties: random, greedy, hillclimber  
-ex / --experiment: het experiment dat je van dat algoritme wilt runnen. de opties hiervoor worden in de tabel hieronder beschreven. 

Gebruik de afkortingen uit deze tabel om in te vullen in bovenstaande format.

|random|-|greedy|-|hillclimber|-|
|------|-|------|-|----------|-|
|afkorting|uitleg|afkorting|uitleg|afkorting|uitleg|
|bs|baseline|bs|baseline|bs|baseline|
|mt|maximum amount of trajectories|smart|smart start station greedy|4_2|delete 4 trajectories, add 2|
|nvc_max|no visited connections, maximum amount of trajectories|rd_greedy|random greedy|nr|no visited connections: no return|
|nvc_random|no visited connections, random amount of trajectories|tr| best trajectory amount|smart_s|smart start station|
|nsr|smart random: not so random|||smart_r|smart removal of trajectories|
|tr|best trajectory amount|||tr|best trajectory amount|
*noot: in bovenstaande tabel worden engelse termen gebruikt om consistent te blijven met de code in main.py*

Om bijvoorbeeld de smart greedy te draaien voor holland, doe dan:
```
$ python3 main.py -k nh -a greedy -ex smart
```
Bij het weglaten van alle argumenten, worden standaard nl, random en baseline gekozen.

voor hulp, run:
```
$ python3 main.py -h
```
of  
```
$ python3 main.py --help
```
  
### Structuur
De belangrijkste bestanden voor het uitvoeren staan in de volgende lijst
* /code: bevat alle code van dit project 
  * /code/algoritmen: bevat de code voor de algoritmes  
  * /code/classes: bevat de klasses voor deze case
* /data: bevat de databestanden om noord holland of nederland mee in te laden
* /experimenten: bevat alle experimenten die zijn uitgevoerd