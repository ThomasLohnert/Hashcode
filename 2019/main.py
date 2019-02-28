import file_io
import os
import random

DEBUG = True

datasets = os.listdir("data")

for dataset in datasets:
    photos = file_io.read_input(dataset)
    slides = []
    last_vertical = None
    photos.sort(key=lambda tup: tup[2])  # sorts in place

    for idn, orientation, num_of_tags, tags in photos:
        #print(idn, orientation, tags)
        if orientation == "V":
            if last_vertical is None:
                last_vertical = (idn, orientation, tags)
            else:
                slides.append((last_vertical[0], idn))
                last_vertical = None
        else:
            slides.append((idn,))

    #random.shuffle(slides)
    print("Started write")
    file_io.write_output(dataset, slides)
    print("finished dataset " + dataset)

print("done")