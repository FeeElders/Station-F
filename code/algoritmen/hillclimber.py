import copy
import random
import csv
from code import helpers

from .randomise import Random 
from .randomise import NotSoRandom 
from code.algoritmen  import randomise as rd
from code.classes.trajectory import Trajectory
from code.classes.station import Station
from code.classes.connection import Connection


from code.classes import station, railway, connection, trajectory


class HillClimber():
    def __init__(self, random_railway) -> None:
        # if not railway.is_valid():
#             raise Exception("HillClimber requires a complete solution.")
        
        
        self.railway = copy.deepcopy(random_railway)
        self.score = self.railway.score()
        self.all_connections = self.railway.get_all_connections()
        self.all_scores: dict[int:int] = {}
        
    def get_start_station(self):
        return random.choice(list(self.railway.get_all_stations()))
        
    def get_random_connection(self, station: 'Station', time: int, new_railway) -> 'Connection':
        connections = new_railway.get_available_connections(station, time)

        if connections is None:
            return None

        choice = random.choice(connections)
        
        return choice
        
    def create_new_train(self, new_railway, traject, random_train):
        
        current_station = self.get_start_station()
        train = Trajectory(current_station, new_railway._max_time)
        new_railway._trains[random_train] = train

        while train.is_running():
            time = train.time_left()

            current_station = train.current_station()
            connection = self.get_random_connection(current_station, time, new_railway)
            if connection == None:
                break
            else:
                train.add_connection(connection)
                
        return new_railway
        
    def remove_old_connections(self, traject):
        """
        from visited connevtions remove the connections that are in de traject we want to change. 
        """
        traject.clear_visited_connections()
        
    def mutate_single_trajectory(self, new_railway):
        """
        Changes the connections of a random traject with a random valid traject.
        """
        # get the key from the traject that is going to change
        random_train = random.choice(list(new_railway._trains.keys()))
        
        # With the key we have acces to the traject object   
        traject = new_railway._trains[random_train] 
        
        # to make a new traject we have to delete the old connections from visited conections  
        self.remove_old_connections(traject)   
        
        new_train = self.create_new_train(new_railway, traject, random_train)
        
        return new_train
        
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

    def check_solution(self, new_railway) -> bool:
        """
        Checks and accepts better solutions than the current solution.
        """
        new_score = new_railway.score()
        old_score = self.score

        # We are looking for maps that score better!
        if new_score >= old_score:
            self.railway = new_railway
            self.score = new_score
            
            return True
            
        return False

    def run(self, run_count, active=False) -> 'Railway': #TODO: iterations toevoegen
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        error_margin = 2
        no_change = 0
        iteration = 0
        while no_change <= error_margin:
        #for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration} and {no_change}, current value: {self.score}') if active else None

            # Create a copy of the railway to simulate the change
            new_railway = copy.deepcopy(self.railway)

            self.mutate_railway(new_railway)

            # Accept it if it is better
            self.check_solution(new_railway)
            
            if self.check_solution(new_railway) == False:
                no_change += 1
            else:
                no_change = 0
            
            self.all_scores[iteration]= self.score
            
            # add score and iterations to csv every 20 iterations
            if iteration%20 == 0 or no_change == error_margin:
                with open(f'output/hillclimber/run_{run_count}.csv', 'a', newline='') as file:
                    writer_new = csv.writer(file)
                    for iteration in self.all_scores:
                        writer_new.writerow([iteration, self.all_scores[iteration]])
                self.all_scores={}
            
            iteration += 1
    
            
        return self.railway
            

