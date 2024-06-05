from stations import Station, Planning, Connection, Trajectory


if __name__ == "__main__":
    print("WELCOME TO RailNL")

    planning = Planning()
    
    planning.print_stations()
    current_station = planning.get_station()
    print(current_station.name)

    planning.get_connections(current_station.name)

    traject1 = Trajectory(current_station, 120)
    print(traject1.time_usage)
    current_station = traject1.current_station

    # stations.get_connections("Amsterdam Sloterdijk")

    # stations.print_all_connections()

    # dit is een verandering b
    
    # stations.get()
    
    
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
