class PizzaSlicer:

    def __init__(self, file_path):
        self.f = open(file_path)
        first_line = self.f.readline()
        params = first_line.split(" ")
        self.rows = int(params[0])
        self.cols = int(params[1])
        self.min_ingredients = int(params[2])
        self.max_slice = int(params[3])
        self.model = self.parse_file()

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

slicer = PizzaSlicer("example.in")
print("rows {}".format(slicer.rows))
print("cols {}".format(slicer.cols))
print("min in {}".format(slicer.min_ingredients))
print("slice size {}".format(slicer.max_slice))