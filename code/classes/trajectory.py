from .connection import Connection
from .station import Station


class Trajectory():
    """ Object for a single trajectory. """
    def __init__(self, station: 'Station', time: int) -> None:
        self._max_time = time
        self._time_usage = 0
        self._current_station = station
        self._trajectory: list['Station'] = [station]
        self._connections: list['Connection'] = []

    def time_left(self) -> int:
        return self._max_time - self._time_usage


    def time_usage(self) -> int:
        """ Calculate the time that trajectory is using. """
        return self._time_usage


    def print_trajectory(self) -> None:
        for station in self._trajectory:
            print(station._name)
    

    def get_trajectory(self) -> list['Station']:
        stations: list['Station'] = []
        for station in self._trajectory:
            stations.append(station)

        return stations
            
    
    def current_station(self) -> 'Station':
        return self._current_station
    
    
    def add_connection(self, connection: 'Connection') -> None:
        """ Add a connection to a trajectory.

        Add end station (string) to the trajectory list
        Change current_station to that end station."""
        
        #renewed version:
        if  connection._station1 == self._current_station:
            self._current_station = connection._station2
        
        else:
            self._current_station = connection._station1
        
        # only add the new station to the list    
        self._trajectory.append(self._current_station)
        
        # add the distance in time to the usage
        self._time_usage += connection._distance
        
        #add connections to self._connection
        self._connections.append(connection)

        
    def get_visited_connections(self) -> list['Connection']:
        return self._connections

    
    def clear_visited_connections(self) -> None:
        self._connections.clear()

        
    def end(self) -> list["station"]:
        """ 
        if no more connections are possible or the time is up
        
        return the list of stations the train will pass and the time that is passed
        """
        print("the trajectory:")
        for each in self._trajectory:
            print(f"{each._name}", end=", ")
        print("\n")

        # TODO: return list of stations. and the distance of the whole trajectory

    def is_running(self) -> bool:
        return self.time_left() > 0
