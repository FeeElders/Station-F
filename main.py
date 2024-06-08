from code.classes import station, railway, connection, trajectory


if __name__ == "__main__":
    print("WELCOME TO RailNL")

    railway = railway.Railway()
    railway.load_stations()
    railway.load_connections()


    # TODO: randomize this 7
    while railway.trains() < 7:
        current_station = railway.get_random_station()
        railway.new_trajectory(current_station, 120)

        train_number = railway.trains()
        traject = railway._trains[train_number]
    

        while traject.is_running():
            time = traject.time_left()
            current_station = traject.current_station()
            connection = railway.get_random_connection(current_station._name, time)
            if connection == None:
                traject.end()
                break

        
            else: 
                traject.add_connection(connection)    
    
    
    print(f"the score: {railway.score()}")


#    railway.formatted_output()


## uiteindelijk deze dingen 10000 keer uitvoeren en plotten om de gemiddelde 
