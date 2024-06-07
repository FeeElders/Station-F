from .connection import Connection
from .station import Station


class Trajectory():
    """ Object for a single trajectory. """
    def __init__(self, station: 'Station', time: int) -> None:
        self.max_time = time
        self.time_usage = 0
        self.current_station = station
        self.trajectory: list['Station'] = [station]

    def time_left(self) -> int:
        return self.max_time - self.time_usage

    def add_connection(self, connection: 'Connection') -> None:
        """ Add a connection to a trajectory.

        Add end station (string) to the trajectory list
        Change current_station to that end station."""

        # # Get all connections for the current station
        # ## DIT WERKT NOG NIET
        # all_connections = planning.get_connections(self.current_station)

        # # Choose a random connection
        # new_connection = random.choice(all_connections)
        
        #renewed version:
        if  connection.station1 == self.current_station:
            self.current_station = connection.station2
        
        else:
            self.current_station = connection.station1
        
        # only add the new station to the list    
        self.trajectory.append(self.current_station)
        
        # add the distance in time to the usage
        self.time_usage += connection.distance
            

        # # add the end station to the trajectory and make it the current station
#         self.trajectory.append(new_connection.station2)
#         self.current_station = new_connection.station2

        # # add the distance in time to the usage
#         self.time_usage += new_connection.distance

    def end(self) -> list["station"]:
        """ 
        if no more connections are possible or the time is up
        
        return the list of stations the train will pass and the time that is passed
        """
        print("the trajectory:")
        for each in self.trajectory:
            print(f"{each.name}", end=", ")
        print("\n")    

    def is_running(self) -> bool:
        return self.time_left() > 0
