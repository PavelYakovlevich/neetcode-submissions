from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.trips = defaultdict(lambda: [0, 0])
        self.active_trips = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.active_trips[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station_name, start_time = self.active_trips[id]
        self.active_trips.pop(id)
        trip_time = t - start_time
        
        trips_count, total_time = self.trips[(start_station_name, stationName)]
        self.trips[(start_station_name, stationName)] = [trips_count + 1, total_time + trip_time] 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trips_count, total_time = self.trips[(startStation, endStation)]

        return total_time / trips_count