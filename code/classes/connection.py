from .station import Station

class Connection():
    """ Object for connections between two stations. """
    def __init__(self, station1: 'Station', station2: 'Station', distance: int) -> None:
        self._station1 = station1
        self._station2 = station2
        self._distance = distance

    def __repr__(self) -> str:
        return f"{self._station1._name} - {self._station2._name}, {self._distance}"
