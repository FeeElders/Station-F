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


    def __repr__(self) -> str:
        return f"{self._trajectory}"

    def time_left(self) -> int:
        """ Get time that is left in trajectory.

        Returns:
        int
        """
        return self._max_time - self._time_usage


    def time_usage(self) -> int:
        """ Calculate the time that trajectory is using.

        Returns:
        int
        """
        return self._time_usage
    

    def get_trajectory(self) -> list['Station']:
        """ Get stations in trajectory.

        Returns:
        list['Station']
        """
        return self._trajectory
    
    def current_station(self) -> 'Station':
        """ Get current station of the trajectory.

        Returns:
        'Station'
        """
        return self._current_station
    
    
    def add_connection(self, connection: 'Connection') -> None:
        """ Add a connection to a trajectory.

        Args:
        connection ('Connection'): the connection to add.
        """
        # update current_station
        if  connection._station1 == self._current_station:
            self._current_station = connection._station2
        
        else:
            self._current_station = connection._station1
        
        # Add the new current station to the trajectory    
        self._trajectory.append(self._current_station)
        
        # Add the distance in time to the usage
        self._time_usage += connection._distance
        
        # Add connection object to self._connection
        self._connections.append(connection)

        
    def get_visited_connections(self) -> list['Connection']:
        """ Get the visited connections of trajectory.

        Returns:
        list['Connection']: the connections that are visited.
        """
        return self._connections

    
    def clear_visited_connections(self) -> None:
        """ Clear trajectory of connections and time usage. """
        self._connections.clear()
        self._time_usage = 0
        self._trajectory = {}


    def is_running(self) -> bool:
        """ Check if trajectory is still within max_time.

        Returns:
        bool
        """
        return self.time_left() > 0
