import numpy as np
import matplotlib

class Ride:
    def __init__(self, start_pos, end_pos, start_time, end_time ):
        self.start_pos =

class RideScheduler:

    def __init__(self, file_path):
        self.f = open(file_path)
        first_line = self.f.readline()
        self.rows, self.cols, self.vehicles, self.rides = first_line.split(" ")

        self.cut(self.model)
        print(self.slices)
        self.f.close()

    def write_result(self):
        out = open("schedule.txt", "w+")

        out.close()

    def calc_distance(self, start, end):
        return abs(start[0]-end[0]) + abs(start[1]-end[0])

    def order_by_start(self,):
