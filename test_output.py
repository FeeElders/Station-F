from stations import Station, Planning, Trajectory, Connection

if __name__ == "__main__":

    print("this is a test railway")

    planning = Planning()

    traject1 = Trajectory("Beverwijk", 120)

    train_1 = {"Beverwijk": "Castricum", "Castricum": "Alkmaar", "Alkmaar": "Hoorn", "Hoorn": "Zaandam"}


    print(f"{planning.connections}\n")
    for key in train_1:
        print(key)
        connection = planning.pick_one_connection(key, train_1[key])
        print(f"station 1: {connection.station1.name}")
        print(f"station 2: {connection.station2.name}")
        traject1.add_connection(connection)

    print(traject1.trajectory)

    
