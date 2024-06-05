from stations import Station, Connection




print("WELCOME TO RailNL")
# Begin met een random station
all_stations = Station()
time = 120 #max minutes


# run 7 trajectories
while True:
    station = all_stations.get_station()
    traject = Connection(station, time)
    
    # allow adding stations as long as the time is not empty
    while traject.is_running():
        traject.add_connection()