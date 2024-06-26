# Station-F
## Case
lijnvoering = trajecten waarover een trein gedurende de dag heen en weer kan rijden
Traject = een route van sporen en stations waarover een trein heen en weer rijdt
mag niet langer zijn dan het opgegeven tijdsframe (120 min per traject Holland en 180 min Nederland).
K = kwaliteit lijnvoering
p = fractie gereden verbindingen ten opzichte van het totaal aan mogelijke verbindingen
T = Het aantal trajecten in de lijnvoering
Min = het totaal aantal gereden minuten 

  K = p*10000 - (T*100 + Min)

## StateSpace
State Space NEDERLAND
180 min max per traject en voor nu gaan we er van uit dat ieder traject deze vol maakt
kortste verbinding is 5 minuten
aantal verbindingen per traject is dus 36 (r=36)
Utrecht centraal heeft 9 mogelijke verbindingen en is daarmee het hoogst. (N=9)
In totaal kunnnen er max 20 trajecten worden gevormd. Omdat het ook mogelijk is om een verschillend aantal trajecten te hebben voor een oplossing, wordt het resultaat van die eerste N en het aantal trajecten r (want kan ook 4 trajecten doen of 7)

Formule voor de trajecten waarbij repetitie kan en volgorde is belangrijk: 
N^r 
9^36 = 2.25 * 10^34

Om te kijken voor verschillende hoeveelheden trajecten doen we de uitkomst keer 20!
9^36 *20! = 5.48093885 * 10^52

Formule voor de hele dienstregeling waarbij repetitie kan en volgorde niet belangrijk is
(r+N-1)!/r!(N-1)!
N = 9^36
r = 20
Resultaat te groot voor rekenmachine om faculteit van te berekenen

## Keuzes
### Random 
Om met de algoritmen te beginnen hebben we een random algoritme gebruikt. Hierbij zijn we er van uit gegaan dat we de volle minuten gebruiken per traject, het is mogelijk om verbingen dubbel te rijden en het aantal trajecten is random. Op basis hiervan zijn we gaan experimenteren met het aantal trajecten vast zetten. Hierbij hebben we gekeken naar het theoretisch aantal nodige stations om alle verbindingen te kunnen rijden. Voor Nederland kwamen we op 9 trajecten uit en voor holland was het theoretisch minimum  4. We kijken bij welk vast aantal trajecten de beste scores worden gehaald. Dit doen we aan de hand van de volledig random en later ook nog op basis van de not so random algortime die later nog verder uitgelegd zal worden. Dit laat zien dat 13 trajecten voor random de beste resultaten geeft. In experimenten waarin we het aantal trajecten vast zetten zullen we dit aantal gebruiken. 

We hebben ook geexperimenteerd met de mogelijkheid om verbindingen niet nog een keer dubbel te bereiden of alleen wanneer het niet anders kan. Deze hebben we op basis van random aantal trajecten gedaan en op basis van het vaste aantal trajecten. Hierbij gaan we er ook nog steeds vauit dat we de volledige tijdsduur benutten tenzij er geen opties meer zijn om te bereiden. 

Als laatste hebben we ook nog gekeken naar het effect van een start station die nog niet eerder is bereikt en verbindingen die in princiepe niet vaker bereden mogen worden tenzij het niet anders kan. Hierbij maken we ook gebruik van het ideale aantal trajecten en wordt in ieder traject de volledige tijd benut.
 
### Greedy
......

### Random Greedy
......

### Hill Climber
Omdat we bij random al zagen dat het aantal trajecten een behoorlijke invloed kon hebben op de range aan resultaten hebben we ook hier geexperimenteerd met het aantal trajecten. De hillclimbers die we hiervoor gebruiken is onze eerste versie van een random basis van max aantal trajecten waarbij 1 random traject wordt verwijderd en 1 random nieuw traject wordt gemaakt. Het is hierbij mogelijk om verbindingen dubbel te rijden en de max tijd word volgemaakt.  

Als tweede hebben we gekeken naar het effect van het verwijderen van 4 trajecten en het leggen van 2 nieuwe trajecten (maar ook hebben we handmatig gekeken), ook deze is weer op basis van een random met het max aantal trajecten en de mogelijkheid om verbindingen dubbel te rijden. 
Dit liet geen verbetering zien dus hebben we voor de rest van de experimenten gebruik gemaakt van 1 traject verwijderen en 1 nieuwe maken.

Om het onderzoek naar het aantal trajecten voort te zetten en zijn we gaan testen voor welke basis aan trajecten de beste scores zijn. Ook hier hebben we voor nederland naar de range van 11 t/m 20 gekeken en voor Holland 4 t/m 7. We hebben dit aan de hand van de basis hillclimber (1 weg 1 erbij) en de smart start hillclimber (die later verder wordt uitgelegd) gerund. Hier kwam uit dat 11 trajecten de beste scores gaf. 
Voor de rest van de experimenten gebruiken we daarom 11 als max aantal trajecten. 

Net als bij random zijn we ook benieuwd wat een verbod op dubbel rijden van verbindingen doet. Hiervoor gebruiken we wel een random basis van max 11 trajecten waarbij trajecten wel dubbel kunnen zijn. Deze worden 1 voor 1 aangepast voor trajecten die geen dubbele verbindingen rijden. Ook hier wordt de max tijd volgemaakt tenzij er geen verbindingen meer kunnen worden gereden. 

Om de resulaten nog verder te verbeteren hebben we hieraan ook een smart start station toegevoegd die ervoor zorgt dat er een beginstation wordt gekozen die het minst aantal mogelijke verbindingen heeft.

Tijdens het plotten van de trajecten zagen we echter dat er stations langs het traject werden overgeslagen. Om dit te verbeteren hebben we een Smart remove heuristiek toe gevoegd die kijkt welke trajectten nog stations hebben met ongereden verbindingen en dat traject wordt dan opnieuw gelegd. Deze heuristiek is op basis van de smart start. 

## Reproduceren resultaten 
In de command line kan je mee geven of je de experimenten voor Nederland (NL) of Holland (NH) wil runnen. Daarnaast kan je ook mee geven welke algoritmen je aan wil zetten en of je voor het trajecten experiment gaat of voor de andere experimenten. 
Voor ieder algoritme bestaat er een experimenten file hier staan alle waarden die nodig zijn om onze resultaten te verkrijgen al in. Je kan dus python3 main.py NL typen om alles te runnen voor Nederland. Als je niks mee geeft draai je de alle experimenten ook voor Nederland. 

Mocht je aanpassingen willen doen om andere resultaten te krijgen dan kan dat in de experimenten zelf. 
