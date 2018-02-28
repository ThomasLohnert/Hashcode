import numpy as np

class Slice:
    def __init__(self, start_row, start_col, end_row, end_col):
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col


class PizzaSlicer:

    def __init__(self, file_path):
        self.f = open(file_path)
        first_line = self.f.readline()
        params = first_line.split(" ")

        self.rows = int(params[0])
        self.cols = int(params[1])
        self.min_ingredients = int(params[2])
        self.max_slice = int(params[3])

        self.model = np.array(self.parse_file())

        self.num_m = len(self.model[self.model == 0])
        self.num_t = len(self.model[self.model == 1])
        
        self.f.close()

    def parse_file(self):
        lines = self.f.readlines()
        matrix = [[0 for x in range(self.cols)] for y in range(self.rows)]
        i = 0
        for line in lines:
            j = 0
            for letter in line:
                if letter == "T":
                    matrix[i][j] = 1
                j += 1

            i += 1
        return matrix

    def write_file(self, slices):
        out = open("output.txt", "w+")
        out.write("{}\n".format(len(slices)))
        for slice in slices:
            out.write("{0} {1} {2} {3}\n".format(slice.start_row, slice.start_col, slice.end_row, slice.end_col))

        out.close()


slicer = PizzaSlicer("example.in")
print("rows {}".format(slicer.rows))
print("cols {}".format(slicer.cols))
print("min in {}".format(slicer.min_ingredients))
print("slice size {}".format(slicer.max_slice))

