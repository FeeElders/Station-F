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
Dit is ook het punt in het verhaal waarin je kort toelicht wat de case lastig maakt 

State Space NEDERLAND
180 min max per traject en voor nu gaan we er van uit dat ieder traject deze vol maakt
kortste verbinding is 5 minuten
aantal verbindingen per traject is dus 36 (r=36)
Utrecht centraal heeft 9 mogelijke verbindingen en is daarmee het hoogst. (N=9)
In totaal kunnnen er max 20 trajecten worden gevormd dus 20! (want kan ook 4 trajecten doen of 7)

Formule repetitie kan en volgorde is belangrijk: 
N^r * 20!
9^36 * 20! = 5,48 * 10^52
