class Ride:
    def __init__(self, id, start_pos, end_pos, start_time, end_time):
        self.id = id
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.start_time = start_time
        self.end_time = end_time
        self.duration = self.calc_distance(start_pos, end_pos)

    def calc_distance(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])