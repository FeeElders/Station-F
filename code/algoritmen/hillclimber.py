import copy

class HillClimber():
    def __init__(self, railway) -> None:
        self.new_railway = copy.deepcopy(railway)

    def run(self) -> 'Railway':
        """ change one aspect every run. """

        # TODO: een functie die dit laat runnen tot de score een aantal iteraties niet meer verbetert.
        # TODO: een aspect elke run veranderen en opnieuw genereren.
            # bijv: als een traject minder dan 4 verbindingen heeft vervang je deze, alleen stopt dit vrij snel wss.
            # andere optie: elke keer het kleinste traject eruit halen en vervangen
            # andere optie: kleinste trajct eruit halen, dan vergelijken of de score beter wordt en behouden of vervangen. Dan pas kiezen of er ook een nieuw traject wordt aangemaakt, misschien wel trajecten blijven verwijderen tot de score niet meer beter wordt. dan komen we misschien op een gemiddeld aantal trajecten dat optimaal is.
        ## De oude railway + score bewaren in een variabele
        ## Deze vergelijken met de nieuwe score en dan vervangen of behouden

    
    
        
