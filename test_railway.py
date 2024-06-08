from code.classes import station, railway, trajectory, connection

if __name__ == "__main__":

    print("this is a test railway")

    railway = railway.Railway()
    railway.load_stations()
    railway.load_connections()

    
    train_1 = {"Beverwijk": "Castricum", "Castricum": "Alkmaar", "Alkmaar": "Hoorn", "Hoorn": "Zaandam"}
    train_2 = {"Amsterdam Sloterdijk": "Amsterdam Centraal", "Amsterdam Centraal": "Amsterdam Amstel", "Amsterdam Amstel": "Amsterdam Zuid", "Amsterdam Zuid": "Schiphol Airport"}
    train_3 = {"Rotterdam Alexander": "Gouda", "Gouda": "Alphen a/d Rijn", "Alphen a/d Rijn": "Leiden Centraal", "Leiden Centraal": "Schiphol Airport", "Schiphol Airport": "Amsterdam Zuid"}

    trains = [train_1, train_2, train_3]

    print(f"{railway._connections}\n")
    for train in trains:
        keys = list(train.keys())
        first_station = railway._stations[keys[0]]
        railway.new_trajectory(first_station, 120)
        traject = railway._trains[railway.trains()]
        for key in train:
            print(key)
            connection = railway.choose_connection(key, train[key])
            print(f"station 1: {connection._station1._name}")
            print(f"station 2: {connection._station2._name}")
            traject.add_connection(connection)
            railway._choices.add(connection)
        print(f"aantal connecties: {len(railway._choices)}")
            
        print(f"het hele traject: {traject._trajectory}")

    
    #railway.formatted_output()
