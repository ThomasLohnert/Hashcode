import os

def read_input(file_name):
    """
    Reads in an input file and returns:
    """
    with open(os.path.join("data/", file_name)) as f:
        lines = f.readlines()
        lines = lines[1:]
        line_parts = [line.split() for line in lines]
        line_parts = [(parts[1], parts[0], parts[2:]) for parts in line_parts]
        return line_parts


def write_output(file_name):
    """
    Writes a list of vehicles as a solution file
    """
    with open(file_name, "w+") as f:
        f.writelines("")
