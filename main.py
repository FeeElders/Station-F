from code.classes import station, planning, connection, trajectory


if __name__ == "__main__":
    print("WELCOME TO RailNL")

    planning = planning.Planning()


    # TODO: randomize this 7
    while planning.counter < 7:
        current_station = planning.get_random_station()
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


## uiteindelijk deze dingen 10000 keer uitvoeren en plotten om de gemiddelde 
