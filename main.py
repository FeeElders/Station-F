from code.classes import station, planning, connection, trajectory


if __name__ == "__main__":
    print("WELCOME TO RailNL")

    planning = planning.Planning()


    # TODO: randomize this 7
    while planning.counter < 7:
        current_station = planning.get_station()
        planning.new_trajectory(current_station, 120)


        traject = planning.trains[planning.counter]
    

        while traject.is_running():
            time = traject.time_left()
            current_station = traject.current_station
            connection = planning.get_connection(current_station.name, time)
            if connection == None:
                traject.end()
                break

        
            else: 
                traject.add_connection(connection)    
    
    
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
