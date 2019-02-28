class Vehicle:
    def __init__(self, id):
        self.id = id
        self.jobs = []
        self.time = 0
        self.last_pos = (0, 0)

    def move(self):
        pass

    def update(self, ride):
        self.jobs.append(ride)
        self.time = self.time + self.calc_distance(self.last_pos, ride.start_pos) + ride.duration
        self.last_pos = ride.end_pos

    def calc_distance(self, start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])