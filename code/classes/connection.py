from .station import Station

class Connection():
    """ Object for connections between two stations. """
    def __init__(self, station1: 'Station', station2: 'Station', distance: int) -> None:
        self.station1 = station1
        self.station2 = station2
        self.distance = distance

    def __repr__(self) -> str:
        return f"{self.station1.name} - {self.station2.name}, {self.distance}"
