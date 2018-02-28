class PizzaSlicer:

    def __init__(self, file_path):
        self.f = open(file_path)
        first_line = self.f.readline()
        params = first_line.split(" ")
        self.rows = params[0]
        self.cols = params[1]
        self.min_ingredients = params[2]
        self.max_slice = params[3]

slicer = PizzaSlicer("example.in")
print("rows {}".format(slicer.rows))
print("cols {}".format(slicer.cols))
print("min in {}".format(slicer.min_ingredients))
print("slice size {}".format(slicer.max_slice))