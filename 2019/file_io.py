import os

def read_input(file_name):
    """
    Reads in an input file and returns:
    """
    with open(os.path.join("data/", file_name)) as f:
        lines = f.readlines()
        lines = lines[1:]
        line_parts = [line.split() for line in lines]
        line_parts = [(i, parts[0], parts[2:]) for i, parts in enumerate(line_parts)]
        return line_parts


def write_output(file_name, id_list):
    """
    Writes a list of vehicles as a solution file
    """
    with open(os.path.join("output/", file_name), "w+") as f:
        f.write(str(len(id_list)))
        f.write("\n")
        for ids in id_list:
                f.write(" ".join(map(str, ids)))
                f.write("\n")
