class Vehicle:
    def __init__(self, id):
        self.pos = (0, 0)
        self.dest = (0, 0)
        self.occupied = None
        self.id = id

        self.rides = list()

    def move(self):
        pass
