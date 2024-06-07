import random
import csv
import pandas as pd

class Station():
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y

        self.connections: dict['Station': 'Connection'] = {}

#    def __repr__(self) -> str:
 #       return f"{self.name}"


class Connection():
    """ Object for connections between two stations. """
    def __init__(self, station1: 'Station', station2: 'Station', distance: int) -> None:
        self.station1 = station1
        self.station2 = station2
        self.distance = distance

    def __repr__(self) -> str:
        return f"{self.station1.name} - {self.station2.name}, {self.distance}"


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


class Planning():
    def __init__(self) -> None:

        self.trains: dict[int: 'Trajectory'] = {}
        self.counter = 0
        self.choices: list['Connection'] = []
        
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
                    
        self.connections = []

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

    def print_all_connections(self) -> None:
        """ print all connections """
        for connection in self.connections:
            print(f"{connection.station1} - {connection.station2}, {connection.distance} min")

    def add_station(self, station: 'Station') -> None:
        """ Add station to all stations """
        self.stations[station.name] = station


    def get_station(self) -> 'Station':
        """
        Choose a random station from the list with stations.
        """
        return random.choice(list(self.stations.values()))


    def create_connection(self, connection: 'Connection') -> None:
        """ Create a new connection between two stations. """
        self.connections.append(connection)


    def pick_one_connection(self, station1: str, station2: str) -> 'Connection':
        """ Get connection object from two station strings. """

        connections = self.connections

        for connection in connections:
            if (connection.station1.name == station1 and connection.station2.name == station2) or (connection.station1.name == station2 and connection.station2.name == station1):
                return connection

        
    def get_connections(self, station: str, time:int) -> 'Connection':
        """ Generate random connection from given station.
         Return connection that fits within the time that is left in the trajectory. """
        self.time = time
        list_connections = []
        for connection in self.connections:
            if (connection.station1.name == station or connection.station2.name == station) and connection.distance <= self.time and connection not in self.choices:
#                print(f"connectie: {connection.station1.name} - {connection.station2.name}")
                list_connections.append(connection)
                
               # print(f"{connection.station1.name} has a connection with {connection.station2.name} that takes {connection.distance} minutes")
        
        #als er geen verbindingen meer mogelijk zijn          
        if not list_connections:
            return None
        
        #list['Connection'] aanpassen naar connection?
        choice = random.choice(list_connections)
        self.choices.append(choice)
#        print(f"random choice: {choice.station1.name} - {choice.station2.name}")
 #       print("all choices:")
   #     for each in self.choices:
  #          print(f"{each.station1.name}-{each.station2.name} ")
        return choice


    def new_trajectory(self, current_station: 'Station', time: int) -> None:
        self.counter += 1
        train = Trajectory(current_station, time)
        self.trains[self.counter] = train


    def formatted_output(self) -> list[str]:
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
                print(f"object: {trajectory_obj}")
                station_objects = trajectory_obj.trajectory
                print(station_objects)

                counter = 1
                for station in station_objects:
                    print(counter)
                    print(f"is dit een string?: {station}")
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

        K = p*10000 - (T*100 + min)

        print(f"trains: {T}")
        print(f"min: {min}")
        print(f"percentage {p}")
        print(self.choices)

        return K
