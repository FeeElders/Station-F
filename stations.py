"""make sure random function can be used"""
import random

class Station():
    def __init__(self, name: str, x: float, y: float) -> None:
        # to do: read csv files with station coördinates
        self.name = name
        self.x = x
        self.y = y

        self.connections: dict[int: 'Station'] = {}

    def add_csv() -> None:
        """ add the stations from the csv file """

    def add_station() -> None:
        
    def get_station() -> str:
        """
        Choose a random station from the dictionary/list with stations.
        """
        return random.choice(self.stations)
        


class Connection(self, station: str, time: int):
    """ Object for connections between two stations. """
    def __init__(self) -> None:
        # to do: read csv file with connections
        self.station = station
        self.time = time
        self.connections: dict[int: 'Station'] = {}
        file = open('ConnectiesHolland.csv', "r")
        for line in file:
            # Save all possible connections in a dict

        file.close()
        
    
    def is_running(self) -> bool:
        """check if still enough time left"""  
        
    def add_connection(self) -> str:
        """ 
        search for a connection with the given station. 
        Give back the onther station in the connection 
        make sure to delete the travel time from the total time 
        """  
        for line in self.connections:
            if self.station in line: # and if time in line below total time
                # add to possebillities 
                
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
        # K = p*10000 - (T*100 + Min)
        
        
        

