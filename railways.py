from stations import Station, Planning, Connection


if __name__ == "__main__":
    print("WELCOME TO RailNL")

    stations = Planning()
    
    stations.print_stations()

    stations.get_connections("Amsterdam Sloterdijk")

    stations.print_all_connections()

    dit is een verandering
    
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
