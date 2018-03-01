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

        for v in self.vehicle_list:
            if len(self.rides) == 0:
                break
            r = self.rides.pop()
            v.update(r)

        while len(self.rides):
            for v in self.vehicle_list:
                if len(self.rides) == 0:
                    break
                r = self.rides.pop()
                v.update(r)

        return self.vehicle_list

