from actual_problem.ride import Ride


def read_input(file_name):
    """
    Reads in an input file and returns: a list of ride objects.
    row, column, vehicle, bonus, steps, list of rides
    """
    with open(file_name) as f:
        rows, columns, vehicles, rides, bonus, steps = f.readline().split()

        lines = f.readlines()
        assert(len(lines) == rides)

        rides = _parse_rides(lines)

        return rows, columns, vehicles, bonus, steps, rides


def _parse_rides(lines):
    rides = list()
    for line in lines:
        values = line.split()
        rides.append(Ride((values[0], values[1]), (values[2], values[3]), values[4], values[5]))
    return rides


def write_output(file_name, vehicles):
    """
    Writes a list of vehicles as a solution file
    """
    with open(file_name) as f:
        pass


def parse_vehicles(vehicles):
    pass