import random
import copy

from .randomise import Random, NotSoRandom

class Greedy():
    def __init__(self, railway: 'Railway') -> None:
        self.railway = copy.deepcopy(railway)


    def get_start_station(self) -> 'Station':
        """ Get random start station """
        return random.choice(list(self.railway.get_all_stations()))

    
    def sort_connections(self, list_connections: list['Connection']) -> dict[int: list['Connection']]:
        """ Sort connections on distance
        Args:
        list_connections (list['Connection']): the available connections
        
        Returns:
        dict[int: list['Connection']
        """
        sorted_connections: dict[int: list['Connection']] = {}

        for connection in list_connections:
            distance = connection.get_distance()

            if distance in sorted_connections.keys():
                sorted_connections[distance].append(connection)
            else:
                sorted_connections[distance] = [connection]

        sorted_connections = dict(sorted(sorted_connections.items()))

        return sorted_connections

    
    def get_longest_connection(self, connections: dict[int:  list['Connection']]) -> 'Connection':
        """ Get longest connection """
        keys = connections.keys()
        len_dict = len(keys)
        
        possible_connections = connections[list(connections.keys())[len_dict-1]]
        if len(possible_connections) > 1:
            return random.choice(possible_connections)

        return possible_connections[0]


    def get_shortest_connection(self, connections: dict[int: list['Connection']]) -> 'Connection':
        """ Get shortest connection """

        # Get first key value pair of the sorted dict
        possible_connections = connections[list(connections.keys())[0]]

        # if more than one connections in the list, choose randomly.
        if len(possible_connections) > 1:
            return random.choice(possible_connections)

        # if only one connection in list, choose that one.
        return possible_connections[0]


    def get_random_connection(self, connections: list['Connection']) -> 'Connection':
        """ Get a random connection """
        return random.choice(connections)

    
    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get connection to add to trajectory

        Args:
        station ('Station'): station to start connection from
        time (int): time that is left in trajectory

        Returns:
        'Connection'
        """
        # Get all available connections
        connections = self.railway.get_available_connections(station, time)
        if connections == None:
            return None
        visited_connections = self.railway.get_all_visited_connections()
        not_visited_connections = list(set(connections) - set(visited_connections))
        
        sorted_connections = self.sort_connections(not_visited_connections)

        if len(sorted_connections) == 0:
            return None
        
        return self.get_shortest_connection(sorted_connections)
        
    def run(self, trains = None) -> 'Railway':
        """ Run greedy algorithm

        Args:
        trains (optional, int): the amount of trajectories
        """ 
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
                    
            
class SmartStartStation(Greedy):
    """ Use heuristics to get smart start station """
    def get_start_station(self) -> 'Station':
        """ Get start station that has the lowest amount of unvisited connections """
        # Get unvisited connections per station
        stations_dict = self.railway.get_unvisited_station_connections()
        # Initialize dictionary for sorted stations
        sorted_station: dict[int: list['Station']] = {}

        # sort stations on the amount of connections they have
        for station in stations_dict:
            connections = stations_dict[station]
            amount_connections = len(connections)
            if amount_connections in sorted_station.keys():
                sorted_station[amount_connections].append(station)
            else:
                sorted_station[amount_connections] = [station]


        # Get a list of the keys of the sorted stations
        list_keys = list(sorted_station.keys())

        # sort the keys
        list_keys.sort()

        # get the lowest amount of connections
        key = list_keys[0]
        
        if key == 0:
            try:
                key = list_keys[1]
            except IndexError:
                choice = random.choice(list(self.railway.get_all_stations()))
        
        
        possible_stations = sorted_station[key]

        if len(possible_stations) == 0:
            choice = random.choice(list(self.railway.get_all_stations()))

        elif len(possible_stations) == 1:
            choice = possible_stations[0]

        else:
            choice = random.choice(possible_stations)

        return choice


class RandomGreedy(SmartStartStation):
    def random_or_greedy(self, unsorted_connections: list['Connection'], sorted_connections: list['Connection']) -> 'Connection':
        """ Choose either a random connection or a greedy connection. """
        seed_numbers = [x for x in range(1000)]
        random_seed = random.choice(seed_numbers)
        random_number = random.random()
        
        if random_number < 0.5:
            connection = self.get_random_connection(unsorted_connections)
        elif random_number < 1.0:
            connection = self.get_shortest_connection(sorted_connections)
        else:
            connection = self.get_longest_connection(sorted_connections)

        return connection


    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get random station or greedy station """
        # Get all available connections
        connections = self.railway.get_available_connections(station, time)
        if connections == None:
            return None

        visited_connections = self.railway.get_all_visited_connections()
        not_visited_connections = list(set(connections) - set(visited_connections))
        
        sorted_connections = self.sort_connections(not_visited_connections)

        if len(sorted_connections) == 0:
            return None


        return self.random_or_greedy(not_visited_connections, sorted_connections)
