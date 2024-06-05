import random
import csv

class Station():
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y

        self.connections: dict['Station': 'Connection'] = {}


class Connection():
    """ Object for connections between two stations. """
    def __init__(self, station1: 'Station', station2: 'Station', distance: int) -> None:
        self.station1 = station1
        self.station2 = station2
        self.distance = distance


class Trajectory():
    """ Object for a single trajectory. """
    def __init__(self, station: 'Station', time: int) -> None:
        self.max_time = time
        self.time_usage = 0
        self.current_station = station.name
        self.trajectory: list[str] = ["station"]

    def time_left(self) -> int:
        return self.max_time - self.time_usage

    def time_usage(self) -> int:
        return self.time_usage

    def add_connection(self, connection: 'Connection') -> None:
        """ Add a connection to a trajectory. """

        # # Get all connections for the current station
        # ## DIT WERKT NOG NIET
        # all_connections = planning.get_connections(self.current_station)

        # # Choose a random connection
        # new_connection = random.choice(all_connections)

        # add the end station to the trajectory and make it the current station
        self.trajectory.append(new_connection.station2)
        self.current_station = new_connection.station2

        # add the distance in time to the usage
        self.time_usage += new_connection.distance


class Planning():
    def __init__(self) -> None:

        self.stations: dict[str: 'Station'] = {}

        # read csv files with station coördinates
        with open("data/StationsHolland.csv") as file:
            reader = csv.reader(file)
        
            # skip the first line
            next(reader)

            # add each station object to all stations list
            for name, x, y in reader:
                station = Station(name, x, y)
                self.stations[station.name] = station
            
        
        self.connections = []

        # Open files with all connections
        with open("data/ConnectiesHolland.csv") as connex:
            reader_connex = csv.reader(connex)
            next(reader_connex)

            for station1, station2, distance in reader_connex:
                # make every connection object twice, for each direction
                connection = Connection(self.stations[station1], self.stations[station2], distance)

                # add connections to the list of all connections
                self.connections.append(connection)
                

    def print_stations(self) -> None:
        """ print all stations. """
        for station in self.stations:
            station_obj = self.stations[station]
            print(f"{station_obj.name}, {station_obj.x}, {station_obj.y}\n")

    def print_all_connections(self) -> None:
        """ print all connections """
        for connection in self.connections:
            print(f"{connection.station1} - {connection.station2}, {connection.distance} min")

    def add_station(self, station: 'Station') -> None:
        """ Add station to all stations """
        self.stations[station.name] = station


    def get_station(self) -> 'Station':
        """
        Choose a random station from the list with stations.
        """
        return random.choice(list(self.stations.values()))


    def create_connection(self, connection: 'Connection') -> None:
        """ Create a new connection between two stations. """
        self.connections.append(connection)


    def get_connections(self, station: str) -> list['Connection']:
        list_connections = []
        for connection in self.connections:
            if connection.station1.name == station or connection.station2.name == station:
                list_connections.append(connection)
                print(f"{connection.station1.name} has a connection with {connection.station2.name} that takes {connection.distance} minutes")

        return list_connections

        
    def is_running(self) -> bool:
        """check if still enough time left"""  
                
    def passed(self) -> str:
        """
        list of all stations that are passed
        """   


    def pattern(self) -> str:
        """ 
        Save the connections
        When the track is complete give back all the connections
        Containing start and finish of each connection and the time passed 
        """
            

    def score(self) -> int:
        """Define score of all trajectories. """
        # K = p*10000 - (T*100 + Min)
        
