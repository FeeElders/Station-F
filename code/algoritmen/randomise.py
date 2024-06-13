import copy
import random


class Random():
    def __init__(self, railway) -> None:
        self.new_railway = copy.deepcopy(railway)


    # generate random start station
    def get_start_station(self):
        return random.choice(list(self.new_railway.get_all_stations()))

    def get_random_connection(self, station: 'Station', time: int) -> 'Connection':
        connections = self.new_railway.get_available_connections(station, time)
        if connections is None:
            return None

        choice = random.choice(connections)
        self.new_railway.add_visited_connection(choice)
        return choice

    def run(self, trains = None) -> 'Railway':

        if trains is None:
            amount = random.randint(1, self.new_railway._max_trains)
        else:
            amount = trains

        while self.new_railway.trains() <= amount:
            current_station = self.get_start_station()
            self.new_railway.new_trajectory(current_station)
            
            train_number = self.new_railway.trains()
            traject = self.new_railway._trains[train_number]
                        

            while traject.is_running():
                time = traject.time_left()
                current_station = traject.current_station()
                connection = self.get_random_connection(current_station, time)
                if connection == None:
#                    traject.end()
                    break
                else: 
                    traject.add_connection(connection)    


        print(f"the score: {self.new_railway.score()}")
        
        return self.new_railway

# class RandomStartStation(Random):
#     def get_random_station(self):
#         ## inherited class
#         return 'Station'
    
class NotSoRandomBaseline(random, greedy):
    def get_start_station(self):
        """ Get start station that has not been accessed before. """
        all_stations = self.new_railway.get_all_stations()
        visited_stations = self.new_railway.get_visited_stations()
        
        return None

    def get_possible_connections(self):
        """ Get connections that are not visited yet. """
        all_connections = self.new_railway.get_all_connections()
        visited_connections = self.new_railway.get_visited_connections()
        possible_connections = all_connections - visited_connections

        return None
