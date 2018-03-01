import numpy as np
import matplotlib

class SomeClass:

    def __init__(self, file_path):
        self.f = open(file_path)
        first_line = self.f.readline()
        a, b, c, d = first_line.split(" ")

        self.cut(self.model)
        print(self.slices)
        self.f.close()

    def write_file(self, slices):
        out = open("output.txt", "w+")

        out.close()
