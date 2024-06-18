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
resultaten = 4.1 *10^-19 
10 ^ 310
Dit lijkt ons niet de juiste methode

## Keuzes
#Hill Climber


