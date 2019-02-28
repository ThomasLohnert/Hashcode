import numpy as np
import matplotlib
import file_io
import operator
from Vehicle import Vehicle

class RideScheduler:

    def __init__(self, rows, columns, num_v, bonus, steps, rides ):
        self.rows = rows
        self.cols = columns
        self.num_v = num_v
        self.bonus = bonus
        self.steps = steps
        self.rides = rides

        self.rides = filter(lambda x: x.duration < 5000, self.rides)

        self.vehicle_list = [Vehicle(i) for i in range(self.num_v)]

    def sort_rides(self):
        self.rides = np.random.shuffle(self.rides)

    def assign_jobs(self):

        for v in self.vehicle_list:
            if len(self.rides) == 0:
                break
            r = self.rides.pop()
            v.update(r)

        while len(self.rides):
            for v in self.vehicle_list:
                if len(self.rides) == 0:
                    break
                r = self.filter_impossible(v)
                if r is None:
                    v.update(self.rides.pop(0))
                else:
                    v.update(r)

        return self.vehicle_list

    def filter_impossible(self, v):

        possible_rides = []
        for i, ride in enumerate(self.rides):
            if ride.end_time > (v.time + self.calc_distance(v.last_pos, ride.start_pos) + ride.duration):
                possible_rides.append((i, self.rides[i]))

        if len(possible_rides) == 0:
            return None

        possible_rides = sorted(possible_rides, key=lambda r: self.calc_distance(r[1].start_pos, v.last_pos))
        best_ride_index = possible_rides[0][0]
        return self.rides.pop(best_ride_index)


    def calc_distance(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])