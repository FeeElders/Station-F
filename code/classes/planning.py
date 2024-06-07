import random
import csv

from .trajectory import Trajectory
from .station import Station
from .connection import Connection

class Planning():
    def __init__(self) -> None:

        self.trains: dict[int: 'Trajectory'] = {}
        self.counter = 0
        self.choices = set()
        
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
                    
        self.connections: list[Connection] = []

        # Open files with all connections
        with open("data/ConnectiesHolland.csv") as connex:
            reader_connex = csv.reader(connex)
            next(reader_connex)

            for station1, station2, distance in reader_connex:
                # make every connection object twice, for each direction
                distance = int(distance)
                connection = Connection(self.stations[station1], self.stations[station2], distance)

                # add connections to the list of all connections
                self.connections.append(connection)
                

    def print_stations(self) -> None:
        """ print all stations. """
        for station in self.stations:
            station_obj = self.stations[station]
            print(f"{station_obj.name}, {station_obj.x}, {station_obj.y}\n")

    def print_connections(self) -> None:
        """ print all connections """
        for connection in self.connections:
            print(f"{connection.station1} - {connection.station2}, {connection.distance} min")

    def add_station(self, station: 'Station') -> None:
        """ Add station to all stations """
        self.stations[station.name] = station


    def get__random_station(self) -> 'Station':
        """
        Choose a random station from the list with stations.
        """
        return random.choice(list(self.stations.values()))


    def create_connection(self, connection: 'Connection') -> None:
        """ Create a new connection between two stations. """
        self.connections.append(connection)


    def choose_connection(self, station1: str, station2: str) -> 'Connection':
        """ Get connection object from two station strings. """

        connections = self.connections

        for connection in connections:
            if (connection.station1.name == station1 and connection.station2.name == station2) or (connection.station1.name == station2 and connection.station2.name == station1):
                return connection

        
    def get_connection(self, station: str, time:int) -> 'Connection':
        """ Generate random connection from given station.
         Return connection that fits within the time that is left in the trajectory. """
        self.time = time
        list_connections = []
        for connection in self.connections:
            if (connection.station1.name == station or connection.station2.name == station) and connection.distance <= self.time and connection not in self.choices:
                list_connections.append(connection)
                        
        #als er geen verbindingen meer mogelijk zijn          
        if not list_connections:
            return None
        
        choice = random.choice(list_connections)
        self.choices.add(choice)

        return choice


    def new_trajectory(self, current_station: 'Station', time: int) -> None:
        self.counter += 1
        train = Trajectory(current_station, time)
        self.trains[self.counter] = train


    def formatted_output(self) -> None:
        """ 
        Save the connections
        When the track is complete give back all the connections
        Containing start and finish of each connection and the time passed 
        """

        stations_string = ""
        
        with open('output.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['train', 'stations'])

            
            for train in self.trains:
                stations_string = "["
                train_id = train
                formatted_id = f"train_{train_id}"
                trajectory_obj = self.trains[train]
                station_objects = trajectory_obj.trajectory

                counter = 1
                for station in station_objects:
                    if counter < len(station_objects):
                        stations_string += f"{station.name}, "
                    else:
                        stations_string += f"{station.name}]"
                    counter += 1

                writer.writerow([formatted_id, stations_string])
            writer.writerow(['score', self.score()])

            
        
    def score(self) -> int:
        """Define score of all trajectories. """

        # set T to the amount of trains
        T = self.counter

        # Set start counter for minutes used
        min = 0
        
        for trajectory in self.trains:
            # add time usage of each trajectory to min
            min += self.trains[trajectory].time_usage

        # set p to the connections that have been accessed 
        p = len(self.choices)/len(self.connections)
#        print(f"connections: {len(self.connections)} vs all choices: {len(self.choices)}")

        K = p*10000 - (T*100 + min)

#        print(f"trains: {T}")
 #       print(f"min: {min}")
  #      print(f"percentage {p}")

        return K
