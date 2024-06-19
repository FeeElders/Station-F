import random
import copy

# TODO: import heuristics for start station
from .randomise import Random, NotSoRandom

class Greedy():
    def __init__(self, railway: 'Railway') -> None:
        self.railway = copy.deepcopy(railway)


    def get_start_station(self) -> 'Station':
        """ Get random start station """
        return random.choice(list(self.railway.get_all_stations()))

    def sort_connections(self, list_connections: list['Connection']) -> dict[int: list['Connection']]:
        sorted_connections: dict[int: list['Connection']] = {}

        for connection in list_connections:
            distance = connection.get_distance()

            if distance in sorted_connections.keys():
                sorted_connections[distance].append(connection)
            else:
                sorted_connections[distance] = [connection]

        sorted_connections = dict(sorted(sorted_connections.items()))

        return sorted_connections

    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get shortest connection """
        # Get all available connections
        connections = self.railway.get_available_connections(station, time)
        if connections == None:
            return None
        
        sorted_connections = self.sort_connections(connections)
        
        possible_connections = sorted_connections[list(sorted_connections.keys())[0]]
        if len(possible_connections) > 1:
            return random.choice(possible_connections)

        return possible_connections[0]
            
        
    def run(self, trains = None) -> 'Railway':
        if trains is None:
            amount = random.randint(1, self.railway._max_trains)
        else:
            amount = trains

        # Fill railway with trajectories
        while self.railway.trains() < amount:

            # Get start station
            start_station = self.get_start_station()

            # make new trajectory with start station
            self.railway.new_trajectory(start_station)

            # Access new trajectory
            train_number = self.railway.trains()
            trajectory = self.railway._trains[train_number]

            # fill trajectory with connections while time is left
            while trajectory.is_running():
                time = trajectory.time_left()
                current_station = trajectory.current_station()
                connection = self.get_connection(current_station, time)
                if connection == None:
                    break
                else:
                    trajectory.add_connection(connection)
        return self.railway


class GetLongestConnection(Greedy):
    """ Get longest connection """
    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        # Get all available connections
        connections = self.railway.get_available_connections(station, time)
        if connections == None:
            return None
        
        sorted_connections = self.sort_connections(connections)

        keys = sorted_connections.keys()
        len_dict = len(keys)
        
        possible_connections = sorted_connections[list(sorted_connections.keys())[len_dict-1]]
        if len(possible_connections) > 1:
            return random.choice(possible_connections)

        return possible_connections[0]
    
                    
            
class SmartStartStation(Greedy):
    """ Use heuristics to get smart start station """
    def get_start_station(self) -> 'Station':

        # get available 
        pass


class RandomGreedy(Greedy, NotSoRandom):
    def random_or_greedy(self, station: 'Station', time: int) -> 'Connection':
        """ Choose either a random connection or a greedy connection. """
        random_number = random.random()

        if random_number < 0.2:
            connection = get_random_connection()
        elif random_number < 0.8:
            connection = get_shortest_connection()
        else:
            connection = get_longest_connection()

        return connection


    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get random station or greedy station """
        return self.random_or_greedy(station, time)
