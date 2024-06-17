import copy
import random
from .randomise import Random
from .randomise import NotSoRandom
from code.classes import station, railway, connection, trajectory


class HillClimber():
    def __init__(self, random_railway) -> None:
        if not railway.is_valid():
            raise Exception("HillClimber requires a complete solution.")
        
        
        self.railway = copy.deepcopy(random_railway)
        self.score = self.railway.score()
        self.all_connections = self.railway.get_all_connections()
        
    def mutate_single_trajectory(self, new_railway):
        """
        Changes the connections of a random traject with a random valid traject.
        """
        # TODO: een aspect elke run veranderen en opnieuw genereren.
            # bijv: als een traject minder dan 4 verbindingen heeft vervang je deze, alleen stopt dit vrij snel wss.
            # andere optie: elke keer het kleinste traject eruit halen en vervangen
            # andere optie: kleinste trajct eruit halen, dan vergelijken of de score beter wordt en behouden of vervangen. Dan pas kiezen of er ook een nieuw traject wordt aangemaakt, misschien wel trajecten blijven verwijderen tot de score niet meer beter wordt. dan komen we misschien op een gemiddeld aantal trajecten dat optimaal is.

    def mutate_railway(self, new_railway, number_of_changes=1):
        """
        Changes the value of a number of trajectories with a random valid traject.
        """
        for _ in range(number_of_changes):
            self.mutate_single_trajectory(new_railway)

    def check_solution(self, new_railway):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_score = new_railway.score()
        old_score = self.score

        # We are looking for maps that cost less!
        if new_score <= old_score:
            self.railway = new_railway
            self.score = new_score

    def run(self, iterations, active=False) -> 'Railway':
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.score}') if verbose else None

            # Create a copy of the railway to simulate the change
            new_railway = copy.deepcopy(self.railway)

            self.mutate_railway(new_railway)

            # Accept it if it is better
            self.check_solution(new_railway)
            

