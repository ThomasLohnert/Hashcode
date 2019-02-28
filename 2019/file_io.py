
def read_input(file_name):
    """
    Reads in an input file and returns:
    """
    with open(file_name) as f:
        _, _, _ = f.readline().split()

        return


def write_output(file_name):
    """
    Writes a list of vehicles as a solution file
    """
    with open(file_name, "w+") as f:
        f.writelines("")
