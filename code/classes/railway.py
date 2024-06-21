import random
import csv

from .trajectory import Trajectory
from .station import Station
from .connection import Connection

class Railway():
    def __init__(self, trains, time) -> None:
        self._max_trains: int = trains
        self._max_time: int = time
        self._trains: dict[int: 'Trajectory'] = {}
        self._stations: dict[str: 'Station'] = {}
        self._connections: list[Connection] = []


    def load_stations(self, station_csv) -> None:
        """ Load stations from csv file to Railway Object."""
        # read csv files with station coÃ¶rdinates
        with open(station_csv) as file:
            reader = csv.reader(file)
        
            # skip the first line (header)
            next(reader)

            # add each station object to all stations list
            for name, x, y in reader:
                station = Station(name, x, y)
                self._stations[station._name] = station

                
    def load_connections(self, connections_csv) -> None:
        """ Load connections from csv file into railway object. """        
        # Open files with all connections
        with open(connections_csv) as connex:
            reader_connex = csv.reader(connex)

            # skip header row
            next(reader_connex)

            for station1, station2, distance in reader_connex:
                # make connection object
                distance = int(float(distance))
                connection = Connection(self._stations[station1], self._stations[station2], distance)

                # add connection to the list of all connections
                self._connections.append(connection)


    def trains(self) -> int:
        return len(list(self._trains.keys()))
                
                
    def print_stations(self) -> None:
        """ print all stations. """
        for station in self._stations:
            station_obj = self._stations[station]
            print(f"{station_obj.name}, {station_obj.x}, {station_obj.y}\n")

            
    def print_connections(self) -> None:
        """ print all connections """
        for connection in self._connections:
            print(f"{connection._station1._name} - {connection._station2._name}, {connection._distance} min")

            
    def print_trajectories(self) -> None:
        for train in self._trains:
            trajectory = self._trains[train]
            print(f"train {train}")
            trajectory.print_trajectory()

            
    def add_station(self, station: 'Station') -> None:
        """ Add station to all stations """
        self._stations[station._name] = station

        
    def get_all_stations(self) -> list['Station']:
        """
        Choose a random station from the list with stations.
        """
        return self._stations.values()

    
    def get_visited_stations(self) -> set['Station']:
        """ Get the stations that are visited. """
        visited_connections = self.get_all_visited_connections()
        visited_stations: list['Station'] = []

        for connection in visited_connections:
            station1 = connection.get_station1()
            station2 = connection.get_station2()
             
            visited_stations.append(station1)
            visited_stations.append(station2)

        return set(visited_stations)
         
    def get_all_connections(self) -> set['Connection']:
        """ Get all existing connections"""
        return set(self._connections)

    
    def get_all_visited_connections(self) -> set['Connection']:
        """ Get the connections that are visited within a railway"""
        visited_connections: list['Connection'] = []

        for train in self._trains:
            trajectory = self._trains[train]
            traject_visited_connections = trajectory.get_visited_connections()
            visited_connections.extend(traject_visited_connections)

        return set(visited_connections)


    def get_unvisited_station_connections(self) -> dict['Station': list['Connection']]:
        """ Get unvisited connections per station """
        
        all_stations = self.get_all_stations()
        
        stations_connections: dict['Station': list['Connection']] = {}
        for station in all_stations:
            stations_connections[station] = []
                                
        all_connections = set(self.get_all_connections())
        visited_connections = set(self.get_all_visited_connections())

        unvisited_connections = all_connections - visited_connections

        for connection in unvisited_connections:
            stations_connections[connection.get_station1()].append(connection)
            stations_connections[connection.get_station2()].append(connection)

        for key in stations_connections:
            set(stations_connections[key])

        return stations_connections
        

    def choose_connection(self, station1: str, station2: str) -> 'Connection':
        """ Get connection object from two station strings. """

        connections = self._connections

        for connection in connections:
            if (connection._station1._name == station1 and connection._station2._name == station2) or (connection._station1._name == station2 and connection._station2._name == station1):
                return connection

    def get_available_connections(self, station: 'Station', time: int) -> list['Connection']:
        time_left = time
        list_connections = []
        station = station

        for connection in self._connections:
            if (connection._station1 == station or connection._station2 == station) and connection._distance <= time_left:                list_connections.append(connection)
                        
        # als er geen verbindingen meer mogelijk zijn          
        if not list_connections:
            return None

        return list_connections


    def new_trajectory(self, current_station: 'Station') -> int:
        train_id = self.trains() + 1
        train = Trajectory(current_station, self._max_time)
        self._trains[train_id] = train

        return train_id


    def delete_trajectory(self, trajectory_number: int) -> None:

        trajectory = self._trains[trajectory_number]
        trajectory.clear_visited_connections()

        self._trains.pop(trajectory_number)


    def formatted_output(self, filename: str, time: int) -> None:
        """ 
        Save the connections
        When the track is complete give back all the connections
        Containing start and finish of each connection and the time passed 
        """

        stations_string = ""
        
        with open(f'output/{filename}', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['train', 'stations'])

            
            for train in self._trains:
                stations_string = "["
                train_id = train
                formatted_id = f"train_{train_id}"
                trajectory_obj = self._trains[train]
                station_objects = trajectory_obj._trajectory

                counter = 1
                for station in station_objects:
                    if counter < len(station_objects):
                        stations_string += f"{station._name}, "
                    else:
                        stations_string += f"{station._name}]"
                    counter += 1

                writer.writerow([formatted_id, stations_string])
            writer.writerow(['score', self.score()]) 
            writer.writerow(['time', time])

    def is_valid(self) -> bool:
        """ Check if the railway is valid."""

        # Check that railway has no more than maximum trains
        return 0 < self.trains() < self._max_trains
 
 
    def score(self) -> int:
        """Define score of all trajectories. """

        # set T to the amount of trains
        T = self.trains()

        # Set start counter for minutes used
        min = 0
        
        for trajectory in self._trains:
            # add time usage of each trajectory to min
            min += self._trains[trajectory].time_usage()

        # set p to the connections that have been accessed 
        p = len(self.get_all_visited_connections())/len(self._connections)

        K = p*10000 - (T*100 + min)

        # print(f"trains: {T}")
        # print(f"min: {min}")
        # print(f"percentage {p}")

        return K
