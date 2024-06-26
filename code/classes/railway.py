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


    def __repr__(self) -> str:
        return f"{self._trains}"
        
    def load_stations(self, station_csv) -> None:
        """ Load stations from csv file to Railway Object."""
        # read csv files with station information
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
        """ Return the number of trains in railway. """
        return len(list(self._trains.keys()))

        
    def get_all_stations(self) -> list['Station']:
        """ Get all imported stations inside railway. """
        return self._stations.values()

    
    def get_visited_stations(self) -> set['Station']:
        """ Get the stations that are visited by any of the trajectories inside railway.

        Returns:
        set('Station'): set of the stations that are visited.
        """
        # Access all visited connections
        visited_connections = self.get_all_visited_connections()
        visited_stations: list['Station'] = []

        # Append stations of each connection to visited_stations
        for connection in visited_connections:
            station1 = connection.get_station1()
            station2 = connection.get_station2()
             
            visited_stations.append(station1)
            visited_stations.append(station2)

        # transform to set to get rid of doubles and return
        return set(visited_stations)
         
    def get_all_connections(self) -> list['Connection']:
        """ Get all imported connections inside railway"""
        return self._connections

    
    def get_all_visited_connections(self) -> set['Connection']:
        """ Get the connections that are visited in any of the trajectories.

        Returns:
        set('Connection')
        """
        # Initiate an empty list for visited connections
        visited_connections: list['Connection'] = []

        # loop over each trajectory inside railway
        for train in self._trains:
            trajectory = self._trains[train]
            trajectory_visited_connections = trajectory.get_visited_connections()

            # extend visited_connections list with another list of visited connections
            visited_connections.extend(trajectory_visited_connections)

        # Return a set to get rid of doubles
        return set(visited_connections)


    def get_unvisited_station_connections(self) -> dict['Station': list['Connection']]:
        """ Get all the unvisited connections, organized per station.

        Returns:
        dict['Station': list['Connection']]: a dictionary of each station that has unvisited connections.
        """
        all_stations = self.get_all_stations()

        # Make a dictionary with all the stations as keys
        stations_connections: dict['Station': list['Connection']] = {}
        for station in all_stations:
            stations_connections[station] = []
                                
        all_connections = set(self.get_all_connections())
        visited_connections = set(self.get_all_visited_connections())

        # Get all unvisited connections by intersecting
        unvisited_connections = all_connections - visited_connections

        # Add unvisited connection to stations_connections for each station
        for connection in unvisited_connections:
            stations_connections[connection.get_station1()].append(connection)
            stations_connections[connection.get_station2()].append(connection)

        # make a set from each list to get rid of doubles
        for key in stations_connections:
            set(stations_connections[key])

        return stations_connections
        

    def choose_connection(self, station1: str, station2: str) -> 'Connection':
        """ Get connection object from two station names.

        Args:
        station1 (str): name of one station
        station2 (str): name of other station

        Returns:
        'Connection': the connection between those two stations"""

        connections = self._connections

        for connection in connections:
            if (connection._station1._name == station1 and connection._station2._name == station2) or (connection._station1._name == station2 and connection._station2._name == station1):
                return connection

    def get_available_connections(self, station: 'Station', time: int) -> list['Connection']:
        """ Get available connections from a specific station within the time.

        Args:
        station ('Station'): station from where the connection is going.
        time (int): time that is left within trajectory

        Returns:
        'Connection'
        """
        time_left = time
        list_connections = []
        station = station

        # Get all connections that have station in it and are within the time
        for connection in self._connections:
            if (connection._station1 == station or connection._station2 == station)and connection._distance <= time_left:
                list_connections.append(connection)
                        
        # Return none if no available connections
        if not list_connections:
            return None

        return list_connections


    def get_unused_train_ids(self) -> list[int]:
        """ Get the train id's that are missing from self._trains.

        Returns:
        list[int]: list of train id's that are not used
        """
        max = self._max_trains
        train_ids = list(self._trains.keys())
        unused_ids: list[int] = []

        
        for id in range(1, max + 1):
            if id not in train_ids:
                unused_ids.append(id)

        return unused_ids
        
    
    def new_trajectory(self, start_station: 'Station') -> int:
        """ Make a new trajectory from a start station.

        Args:
        start_station ('Station')

        Returns:
        int: the train number
        """
        train_numbers = self.get_unused_train_ids()
        train_id = train_numbers[0]
        train = Trajectory(start_station, self._max_time)
        self._trains[train_id] = train

        return train_id


    def delete_trajectory(self, trajectory_number: int) -> None:
        """ Delete trajectory from railway.

        Args:
        trajectory_number (int): the trajectory ID
        """
        trajectory = self._trains[trajectory_number]

        # Clear the trajectory before deleting
        trajectory.clear_visited_connections()

        # Delete the trajectory from the dictionary
        self._trains.pop(trajectory_number)


    def formatted_output(self, filename: str, time: int) -> None:
        """ Save the railway to CSV in a formatted string output. """

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
        """ Check if the railway has the correct amount of trajectories."""

        # Check that railway has no more than maximum trains
        return 0 < self.trains() < self._max_trains
 
 
    def score(self) -> int:
        """ Calculate the score of the railway.

        Returns:
        int"""

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
