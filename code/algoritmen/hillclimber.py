import copy
import random
# from .randomise import Random as rd
# from .randomise import NotSoRandom as nsr
from code.algoritmen  import randomise as rd

from code.classes import station, railway, connection, trajectory


class HillClimber():
    def __init__(self, random_railway) -> None:
        # if not railway.is_valid():
#             raise Exception("HillClimber requires a complete solution.")
        
        
        self.railway = copy.deepcopy(random_railway)
        self.score = self.railway.score()
        self.all_connections = self.railway.get_all_connections()
        
    def get_start_station(self):
        return random.choice(list(self.railway.get_all_stations()))
        
    def create_new_train(self, new_railway, traject):
        
        start_station = self.get_start_station()
        Trajectory(start_station, new_railway._max_time)
        
        while traject.is_running():
            time = traject.time_left()
            current_station = traject.current_station()
            connection = self.get_random_connection(current_station, time)
            if connection == None:
                break
            else:
                traject.add_connection(connection)
        
    def mutate_single_trajectory(self, new_railway):
        """
        Changes the connections of a random traject with a random valid traject.
        """
        random_train = random.choice(list(new_railway._trains.keys()))   
        
        traject = new_railway._trains[random_train]     
        new_train = self.create_new_train(new_railway, traject)
        
        new_railway._trains[random_train] = new_train
        
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

        # We are looking for maps that score better!
        if new_score >= old_score:
            self.railway = new_railway
            self.score = new_score

    def run(self, iterations, active=False) -> 'Railway':
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.score}') if active else None

            # Create a copy of the railway to simulate the change
            new_railway = copy.deepcopy(self.railway)

            self.mutate_railway(new_railway)

            # Accept it if it is better
            self.check_solution(new_railway)
            

