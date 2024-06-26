from .station import Station

class Connection():
    """ Object for connections between two stations. """
    def __init__(self, station1: 'Station', station2: 'Station', distance: int) -> None:
        self._station1 = station1
        self._station2 = station2
        self._distance = distance

    def __repr__(self) -> str:
        """ represent connection object as formatted string."""
        return f"{self._station1._name} - {self._station2._name}, {self._distance}"

    def get_station1(self) -> 'Station':
        """ Get station 1 object.

        Returns:
        'Station'
        """
        return self._station1

    def get_station2(self) -> 'Station':
        """ Get station 1 object.
        
        Returns:
        'Station'
        """
        return self._station2

    def get_distance(self) -> int:
        """ Get distance of connection.

        Returns:
        int: distance between station 1 and station 2.
        """
        return self._distance
