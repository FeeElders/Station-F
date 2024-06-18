import copy
import random


class Random():
    def __init__(self, railway) -> None:
        self.new_railway = copy.deepcopy(railway)


    def get_start_station(self):
        """Generate random start station"""
        return random.choice(list(self.new_railway.get_all_stations()))

    
    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get a random connection from available connections """
        # Get all available connections
        connections = self.new_railway.get_available_connections(station, time)
        if connections is None:
            return None

        # Pick one random
        choice = random.choice(connections)

        # Add connection to visited_connections
        self.new_railway.add_visited_connection(choice)
        
        return choice

    def run(self, trains = None) -> 'Railway':
        """ run random algorithm. """
        if trains is None:
            amount = random.randint(1, self.new_railway._max_trains)
        else:
            amount = trains - 1

        # loop for each train/trajectory
        while self.new_railway.trains() <= amount:

            # get start station
            current_station = self.get_start_station()

            # make new trajectory with start station
            self.new_railway.new_trajectory(current_station)

            # access new trajectory
            train_number = self.new_railway.trains()
            traject = self.new_railway._trains[train_number]
                        
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


        print(f"the score: {self.new_railway.score()}")
        
        return self.new_railway


class NoVisitedConnections(Random):
    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get connection that is not visited yet. """
        visited_connections = self.new_railway.get_visited_connections()
        available_connections = self.new_railway.get_available_connections(station, time)

        if available_connections:
            possible_connections = list(set(available_connections) - set(visited_connections))
            choice = random.choice(possible_connections)
#            self.new_railway.add_visited_connection(choice)
            return choice

        else:
            return None
        
    
class NotSoRandom(Random):
    def get_start_station(self):
        """ Get start station that has not been accessed before. """
        all_stations = self.new_railway.get_all_stations()
        visited_stations = self.new_railway.get_visited_stations()
        if not visited_stations:
            return random.choice(list(self.new_railway.get_all_stations()))
        

    def get_connection(self, station: 'Station', time: int) -> 'Connection':
        """ Get a connection that is not visited yet, but if not possible: get visited connection. """
        available_connections = self.new_railway.get_available_connections(station, time)
        visited_connections = self.new_railway.get_visited_connections()
        print(f"visited connections: {visited_connections}")
        print(f"all_connections: {available_connections}")
        if not available_connections:
            return None

        else:
            possible_connections = list(set(available_connections) - set(visited_connections))
            print(f"possible connections: {possible_connections}")
            if not possible_connections:
                choice = random.choice(available_connections)
            else:
                choice = random.choice(possible_connections)

        self.new_railway.add_visited_connection(choice)        
        return choice
