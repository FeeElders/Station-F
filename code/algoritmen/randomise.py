import copy
import random


class Random():
    def __init__(self, railway) -> None:
        self.railway = copy.deepcopy(railway)


    def get_start_station(self):
        """Generate random start station"""
        return random.choice(list(self.railway.get_all_stations()))

    
    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get a random connection from available connections """
        # Get all available connections
        connections = self.railway.get_available_connections(station, time)
        if connections is None:
            return None

        # Pick one random
        choice = random.choice(connections)
        
        return choice

    def run(self, trains = None) -> 'Railway':
        """ run random algorithm. """
        if trains is None:
            amount = random.randint(1, self.railway._max_trains)
        else:
            amount = trains

        # loop for each train/trajectory
        while self.railway.trains() < amount:

            # get start station
            current_station = self.get_start_station()

            # make new trajectory with start station
            self.railway.new_trajectory(current_station)

            # access new trajectory
            train_number = self.railway.trains()
            traject = self.railway._trains[train_number]
                        
            # fill trajectory with connections while time is left
            while traject.is_running():
                time = traject.time_left()
                current_station = traject.current_station()
                connection = self.get_connection(current_station, time)
                if connection == None:
#                    traject.end()
                    break
                else: 
                    traject.add_connection(connection)    

        return self.railway


class NoVisitedConnections(Random):
    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get connection that is not visited yet. """
        visited_connections = self.railway.get_all_visited_connections()
        available_connections = self.railway.get_available_connections(station, time)

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


class NotSoRandom(Random):
    def get_start_station(self):
        """ Get start station that has not been accessed before. """
        all_stations = self.railway.get_all_stations()
        visited_stations = self.railway.get_visited_stations()
        
        if not visited_stations:
            choice = random.choice(list(self.railway.get_all_stations()))

        else:
            possible_stations = list(set(all_stations) - set(visited_stations))
            if possible_stations:
                choice = random.choice(possible_stations)
                
            else:
                choice = random.choice(list(self.railway.get_all_stations()))

        return choice

    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get a connection that is not visited yet, but if not possible: get visited connection. """
        available_connections = self.railway.get_available_connections(station, time)
        visited_connections = self.railway.get_all_visited_connections()

        
        if not available_connections:
            return None

        if not visited_connections:
            return random.choice(available_connections)
        
        else:
            possible_connections = list(set(available_connections) - set(visited_connections))
            if not possible_connections:
                choice = random.choice(available_connections)
            else:
                choice = random.choice(possible_connections)

        return choice
