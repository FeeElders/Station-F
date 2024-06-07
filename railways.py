from stations import Station, Planning, Connection, Trajectory


if __name__ == "__main__":
    print("WELCOME TO RailNL")

    planning = Planning()
    
    planning.print_stations()

    while planning.counter < 7:
        current_station = planning.get_station()
        planning.new_trajectory(current_station, 120)

        print(f"new train!!!! {planning.counter}")
        print(f"new starting point: {current_station.name}")
        

        traject1 = planning.trains[planning.counter]
    

        while traject1.is_running():
            time = traject1.time_left()
            print(f"time left: {time}")
            current_station = traject1.current_station
            connection = planning.get_connections(current_station.name, time)
            if connection == None:
                print("traject voorbij!")
                traject1.end()
                break

        
            else: 
                traject1.add_connection(connection)
                print("traject tot nu toe:")
                for station in traject1.trajectory:
                   print(f"{station.name}", end=", ")
                    
                print("\n")
    
    
    
    print(f"the score: {planning.score()}")


    planning.formatted_output()
    
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



## uiteindelijk deze dingen 10000 keer uitvoeren en plotten om de gemiddelde 
