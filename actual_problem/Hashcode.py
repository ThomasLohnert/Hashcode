import numpy as np
import matplotlib
import file_io
from Vehicle import Vehicle

class RideScheduler:

    def __init__(self, rows, columns, num_v, bonus, steps, rides ):
        self.rows = rows
        self.cols = columns
        self.num_v = num_v
        self.bonus = bonus
        self.steps = steps
        self.rides = rides

        self.vehicle_list = [Vehicle(i) for i in range(self.num_v)]

    def assign_jobs(self):
        while len(self.rides):
            for v in self.vehicle_list:
                if len(self.rides) == 0:
                    break
                r = self.rides.pop()
                v.jobs.append(r)

        return self.vehicle_list

    def calc_distance(self, start, end):
        return abs(start[0]-end[0]) + abs(start[1]-end[0])

    def order_by_start(self,):
        pass