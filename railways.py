from stations import Station, Planning, Connection, Trajectory


if __name__ == "__main__":
    print("WELCOME TO RailNL")

    planning = Planning()
    
    planning.print_stations()

    while planning.counter <= 7:
        print(f"new train!!!! {planning.counter}")
        current_station = planning.get_station()
        print(f"new starting point: {current_station.name}")
        
        
        planning.new_trajectory(planning.counter, current_station, 120)
        traject1 = planning.trains[planning.counter]
   
   
    
        # is dit nou ook het object?

        while traject1.is_running():
            time = traject1.time_left()
            print(f"time left: {time}")
            current_station = traject1.current_station
            connection = planning.get_connections(current_station.name, time)
            if connection == None:
                print("traject voorbij!")
                traject1.end()
                planning.counter += 1
                break
        
            else: 
                traject1.add_connection(connection)
                print("traject tot nu toe:")
                for station in traject1.trajectory:
                   print(f"{station.name}", end=", ")
                    
                print("\n")
    
    
    
    
    
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
