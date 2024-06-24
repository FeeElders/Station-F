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
    def __init__(self, railway: 'Railway') -> None:
        # if not railway.is_valid():
#             raise Exception("HillClimber requires a complete solution.")
        
        
        self.old_railway = copy.deepcopy(railway)
        self.new_railway = None
        self.score = self.old_railway.score()
        self.all_connections = self.old_railway.get_all_connections()
        self.all_scores: dict[int:int] = {}
        
    def get_start_station(self) -> 'Station':
        """ Get random start station.

        Returns:
         'Station'
        """
        return random.choice(list(self.new_railway.get_all_stations()))
        
    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get random connection from given station within given time.

        Args:
        station ('Station')
        time (int)

        Returns:
        'Connection'
        """
        connections = self.new_railway.get_available_connections(station, time)

        if connections is None:
            return None

        choice = random.choice(connections)
        
        return choice
        
    def create_new_train(self) -> None:
        """ Create and fill new trajectory with connections in new railway. """
        current_station = self.get_start_station()
        train_id = self.new_railway.new_trajectory(current_station)
        train = self.new_railway._trains[train_id]

        while train.is_running():
            time = train.time_left()

            current_station = train.current_station()
            connection = self.get_connection(current_station, time)
            if connection == None:
                break
            else:
                train.add_connection(connection)

        
    def remove_single_trajectory(self) -> None:
        """ Removes a random trajectory from new railway. """
                    
        # get the key from the trajectory that is going to change
        random_train = random.choice(list(self.new_railway._trains.keys()))
        
        # delete trajectory from dictionary
        self.new_railway.delete_trajectory(random_train)
        
            
    def add_single_trajectory(self) -> 'Trajectory':
        """ Add random trajectory.

        Returns:
        'Trajectory'
        """

        new_train = self.create_new_train()
    
        return new_train  
    

    def mutate_railway(self, delete, add) -> None:
        """ Delete from or add to new railway any number of trajectories.

        Args:
        delete (int): the number of trajectories to delete
        add (int): the number of trajectories to add
        """
        for _ in range(delete):
            self.remove_single_trajectory()
            
        for _ in range(add):
            self.add_single_trajectory()

    def check_solution(self) -> bool:
        """ Check if new railway is better than the old railway and if so, replace the old with the new railway.

        Returns:
        bool: true if new railway is better or the same as old railway. False if new railway is worse than the old railway.
        """
        new_score = self.new_railway.score()
        old_score = self.score

        # We are looking for maps that score better!
        if new_score >= old_score:
            self.old_railway = self.new_railway
            self.score = new_score
            
            return True
            
        return False

    def run(self, run_count, name, delete, add, active=False) -> 'Railway':
        """ Run hillclimber algorithm until there's N times no change.

        Args:
        run_count (int): which run this hillclimber is part of, for saving purposes.
        name (str): name of the file it's saved in.
        delete (int): the amount of trajectories to delete each iteration.
        add (int): the amount of trajectories to add each iteration.
        active (bool): optional bool to activate a print statement.

        Returns:
        'Railway'
        """
        error_margin = 10000
        no_change = 0
        iteration = 0
        while no_change <= error_margin:
        #for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration} and {no_change}, current value: {self.score}') if active else None

            # Create a copy of the railway to simulate the change
            self.new_railway = copy.deepcopy(self.old_railway)

            self.mutate_railway(delete, add)

            # Accept it if it is better
            self.check_solution()

            # Keep track of how often there is no change
            if not self.check_solution():
                no_change += 1
            else:
                no_change = 0
            
            self.all_scores[iteration]= self.score
            
            # add score and iterations to csv every 20 iterations
            if iteration%1000 == 0 or no_change == error_margin:
                print(f"iteration {iteration} and no change {no_change}, current score: {self.score}")
                with open(f'output/hillclimber/{name}_run_{run_count}.csv', 'a', newline='') as file:
                    writer_new = csv.writer(file)
                    for iteration in self.all_scores:
                        writer_new.writerow([iteration, self.all_scores[iteration]])
                self.all_scores={}
            
            iteration += 1
            
    
            
        return self.old_railway
            
class NoReturn(HillClimber):
    
    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get connection that is not visited yet.

        Args:
        station ('Station')
        time (int)

        Returns:
        'Conenction'"""
        visited_connections = self.new_railway.get_all_visited_connections()
        available_connections = self.new_railway.get_available_connections(station, time)

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
    
    def get_start_station(self) -> 'station':
        """ Get start station based on smart start heuristic.

        Returns:
        'Station'
        """
        stations_dict = self.new_railway.get_unvisited_station_connections()
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

class SmartRemove(NoReturn):
    
    def remove_single_trajectory(self):
        
        # get the key from the trajectory that is going to change that has stations with unvisited connections
        uvisited_station_connection_dict = self.new_railway.get_unvisited_station_connections()
        stations = list(uvisited_station_connection_dict.keys())

        # TODO: for each station:
        # loop door trajecten en kijk welke dit station bevatten
        # self.new_railway.get_trajectory_parent(station())
        #     trajectory = choose one trajectory
        
        # delete trajectory from dictionary
        # self.new_railway.delete_trajectory(trajectory)
        pass
        
class SmallRemove(NoReturn):
    
    def mutate_railway(self):
        """ Add stations to the front of a trajectory """
        
        # get the key from the trajectory that is going to change
        random_train = random.choice(list(self.new_railway._trains.keys()))
        
        # alter trajectory 
        self.alter(random_train)
        
    def alter(self):
        """ change within traject"""
        
        
        
