import copy
import random
import csv
from code import helpers

from code.algoritmen.randomise import Random, NotSoRandom, NoVisitedConnections  
from code.algoritmen  import randomise as rd
from code.classes.trajectory import Trajectory
from code.classes.station import Station
from code.classes.connection import Connection
from code.visualisation import visuals 


from code.classes import station, railway, connection, trajectory


class HillClimber():
    def __init__(self, random_railway) -> None:
        # if not railway.is_valid():
#             raise Exception("HillClimber requires a complete solution.")
        
        
        self.railway = copy.deepcopy(random_railway)
        self.score = self.railway.score()
        self.all_connections = self.railway.get_all_connections()
        self.all_scores: dict[int:int] = {}
        
    def get_start_station(self, new_railway):
        return random.choice(list(new_railway.get_all_stations()))
        
    def get_connection(self, station: 'Station', time: int, new_railway) -> 'Connection':
        connections = new_railway.get_available_connections(station, time)

        if connections is None:
            return None

        choice = random.choice(connections)
        
        return choice
        
    def create_new_train(self, new_railway):
        
        current_station = self.get_start_station(new_railway)
        train_id = new_railway.new_trajectory(current_station)
        train = new_railway._trains[train_id]

        while train.is_running():
            time = train.time_left()

            current_station = train.current_station()
            connection = self.get_connection(current_station, time, new_railway)
            if connection == None:
                break
            else:
                train.add_connection(connection)
                
        return new_railway
        
        
    def remove_single_trajectory(self, new_railway):
        """
        removes a random traject.
        """
                    
        # get the key from the traject that is going to change
        random_train = random.choice(list(new_railway._trains.keys()))
        
        # delete traject from dictionary
        new_railway.delete_trajectory(random_train)
        
            
    def add_single_trajectory(self, new_railway):
        """
        add random valid traject.
        """

        new_train = self.create_new_train(new_railway)
    
        return new_train  
    

    def mutate_railway(self, new_railway, delete, add):
        """
        Changes the value of a number of trajectories with a random valid traject.
        """
        for _ in range(delete):
            self.remove_single_trajectory(new_railway)
            
        for _ in range(add):
            self.add_single_trajectory(new_railway)

    def check_solution(self, new_railway) -> bool:
        """
        Checks and accepts better solutions than the current solution.
        """
        new_score = new_railway.score()
        old_score = self.score

        # We are looking for maps that score better!
        if new_score > old_score:
            self.railway = new_railway
            self.score = new_score
            return True
            
        return False

    def run(self, run_count, name, delete, add, active=False) -> 'Railway': #TODO: iterations toevoegen
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        error_margin = 1000
        no_change = 0
        iteration = 0
        while no_change <= error_margin:
        #for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration} and {no_change}, current value: {self.score}') if active else None

            # Create a copy of the railway to simulate the change
            new_railway = copy.deepcopy(self.railway)

            self.mutate_railway(new_railway, delete, add)

            # Accept it if it is better
            self.check_solution(new_railway)
            
            if self.check_solution(new_railway) == False:
                no_change += 1
            else:
                no_change = 0
            
            self.all_scores[iteration]= self.score
            
            # add score and iterations to csv every 20 iterations
            if iteration%20 == 0 or no_change == error_margin:
                with open(f'output/hillclimber/{name}_run_{run_count}.csv', 'a', newline='') as file:
                    writer_new = csv.writer(file)
                    for iteration in self.all_scores:
                        writer_new.writerow([iteration, self.all_scores[iteration]])
                self.all_scores={}
            
            iteration += 1
            
    
            
        return self.railway
            
class NoReturn(HillClimber):
    
    def get_connection(self, station: 'Station', time: int, new_railway) -> 'Connection':
        """ Get connection that is not visited yet. """
        visited_connections = new_railway.get_all_visited_connections()
        available_connections = new_railway.get_available_connections(station, time)

        if not available_connections:
            return None

        elif not visited_connections:
            choice = random.choice(available_connections)

        else:
            possible_connections = list(set(available_connections) - set(visited_connections))
            if possible_connections:
                choice = random.choice(possible_connections)
            else:
                return None
        return choice
        
        
class SmartStart(NoReturn):
    
    def get_start_station(self, new_railway) -> 'station':
        stations_dict = new_railway.get_unvisited_station_connections()
        minimal_station: dict[int: list['Station']] = {}
        
        for station in stations_dict:
            connections = stations_dict[station]
            amount_connections = len(connections)
            if amount_connections in minimal_station.keys():
                minimal_station[amount_connections].append(station)
            else:
                minimal_station[amount_connections] = [station]


        list_keys = list(minimal_station.keys())
        list_keys.sort(reverse=True)
        key = list_keys[0]
        if key == 0:
            try:
                key = list_keys[1]
            except IndexError:
                return None
        
        
        possible_stations = minimal_station[key]
        if len(possible_stations) == 0:
            choice = None

        elif len(possible_stations) == 1:
            choice = possible_stations[0]

        else:
            choice = random.choice(possible_stations)

        return choice


        
        
        