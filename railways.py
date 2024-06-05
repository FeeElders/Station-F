from stations import Station, Planning, Connection, Trajectory


if __name__ == "__main__":
    print("WELCOME TO RailNL")

    planning = Planning()
    
    planning.print_stations()
    current_station = planning.get_station()
    print(current_station.name)
    
    
    traject1 = Trajectory(current_station, 120)
    time = traject1.time_left()
    print(time)
    current_station = traject1.current_station
    
    # is dit nou ook het object? 
    connection = planning.get_connections(current_station.name, time)
    if connection == None:
        traject1.end()
        
    else: 
        traject1.add_connection(connection) 
    
    
    
    
    
    # # Begin met een random station
# all_stations = Station()
# time = 120 #max minutes


# # run 7 trajectories
# while True:
#     station = all_stations.get_station()
#     traject = Connection(station, time)
    
#     # allow adding stations as long as the time is not empty
#     while traject.is_running():
#         traject.add_connection()
