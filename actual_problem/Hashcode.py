import numpy as np
import matplotlib
import file_io
from Vehicle import Vehicle

class RideScheduler:

    def __init__(self, file_path):
        self.rows, self.columns, self.num_v, self.bonus, self.steps, self.rides = file_io.read_input("b_should_be_easy.in")
        self.vehicle_list = [Vehicle(i) for i in range(self.num_v)]


    def assign_jobs(self):
        num_rides = len(self.rides)
        num_batches = num_rides / self.num_v

        for v in self.vehicle_list:
            i = v.id
            v.jobs = self.rides[num_batches*i:num_batches*(i+1)]

    def calc_distance(self, start, end):
        return abs(start[0]-end[0]) + abs(start[1]-end[0])

    def order_by_start(self,):
