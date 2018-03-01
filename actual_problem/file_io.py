from actual_problem.ride import Ride

def read_input(file_name):
    """
    Reads in an input file and returns a creates a list of ride objects.
    """
    with open(file_name) as f:
        rows, columns, vehicles, rides, bonus, steps = f.readline().split()

        rides = list()

        lines = f.readlines()
        assert(len(lines) == rides)
        for line in lines:
            rides.append(Ride())
        return matrix