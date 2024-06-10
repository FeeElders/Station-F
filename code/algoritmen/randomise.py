import copy

def random(railway) -> 'Railway':
# TODO: randomize this 7
    new_railway = copy.deepcopy(railway)
    while new_railway.trains() < 7:
        current_station = new_railway.get_random_station()
        new_railway.new_trajectory(current_station, 120)

        train_number = new_railway.trains()
        traject = new_railway._trains[train_number]
    

        while traject.is_running():
            time = traject.time_left()
            current_station = traject.current_station()
            connection = new_railway.get_random_connection(current_station._name, time)
            if connection == None:
                traject.end()
                break

        
            else: 
                traject.add_connection(connection)    
    
    
    print(f"the score: {new_railway.score()}")

    return new_railway
