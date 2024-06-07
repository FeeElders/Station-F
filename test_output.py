from stations import Station, Planning, Trajectory, Connection

if __name__ == "__main__":

    print("this is a test railway")

    planning = Planning()

    train_1 = {"Beverwijk": "Castricum", "Castricum": "Alkmaar", "Alkmaar": "Hoorn", "Hoorn": "Zaandam"}
    train_2 = {"Amsterdam Sloterdijk": "Amsterdam Centraal", "Amsterdam Centraal": "Amsterdam Amstel", "Amsterdam Amstel": "Amsterdam Zuid", "Amsterdam Zuid": "Schiphol Airport"}
    train_3 = {"Rotterdam Alexander": "Gouda", "Gouda": "Alphen a/d Rijn", "Alphen a/d Rijn": "Leiden Centraal", "Leiden Centraal": "Schiphol Airport", "Schiphol Airport": "Amsterdam Zuid"}

    trains = [train_1, train_2, train_3]

    print(f"{planning.connections}\n")
    for train in trains:
        keys = list(train.keys())
        first_station = planning.stations[keys[0]]
        planning.new_trajectory(first_station, 120)
        traject = planning.trains[planning.counter]
        for key in train:
            print(key)
            connection = planning.pick_one_connection(key, train[key])
            print(f"station 1: {connection.station1.name}")
            print(f"station 2: {connection.station2.name}")
            traject.add_connection(connection)
            planning.choices.append(connection)
            
        print(f"het hele traject: {traject.trajectory}")

    
    planning.formatted_output()
