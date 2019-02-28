import numpy as np
import math

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

        self.slices = list()

        self.cut(self.model)
        print(self.slices)
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

    def cut(self, pizza, top_left=(0, 0)):
        print("cutting {}".format(top_left))
        row, col = pizza.shape
        if pizza.size <= self.max_slice:
            self.slices.append((top_left[0], top_left[1], top_left[0] + row, top_left[1] + col))
            return

        cutting_vert = row < col

        if cutting_vert:
            length = col
        else:
            length = row

        centre = int(np.ceil(length / 2.0))

        left, right = self.create_slices(pizza, centre, cutting_vert)

        inverted = False
        off = 1
        idx = centre
        while not(self.check_ingredients(left) and self.check_ingredients(right)):
            idx = centre - off
            print("cutting vertically: ", cutting_vert)
            print("cutting at ", str(idx))
            off = -(off + 1)
            if idx >= length or idx < 0:
                if inverted:
                    print(top_left, " invalid")
                    return
                cutting_vert = not cutting_vert
                inverted = True
                off = 0
                centre = int(np.ceil((col / 2.0 if cutting_vert else row / 2.0)))
            left, right = self.create_slices(pizza, idx, cutting_vert)

        if cutting_vert:
            new_top = (top_left[0], top_left[1] + idx)
        else:
            new_top = (top_left[0] + idx, top_left[1])
        self.cut(left, top_left)
        self.cut(right, new_top)

    def create_slices(self, pizza, idx, is_vertical):
        if is_vertical:
            return pizza[:, :idx], pizza[:, idx:]
        else:
            return pizza[:idx, :], pizza[idx:, :]

    def check_ingredients(self, slice):
        true_size = len(slice[slice==1])
        false_size = slice.size - true_size
        return true_size >= self.min_ingredients \
               and false_size >= self.min_ingredients

    def compare_slice(self, left, right):
        ratio_left = left


slicer = PizzaSlicer("small.in")
print("rows {}".format(slicer.rows))
print("cols {}".format(slicer.cols))
print("min in {}".format(slicer.min_ingredients))
print("slice size {}".format(slicer.max_slice))

