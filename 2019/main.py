import file_io
import os
import sorting
import random
import pairing

DEBUG = True

def convert_to_slides(photos_tuples):
    out = []
    for photos in photos_tuples:
        out.append(photos[0])
    return out

datasets = os.listdir("data")

for dataset in datasets:
    print("Started data set {}".format(dataset))
    photos = file_io.read_input(dataset)

    vertical = list(filter(lambda item: item[1] == "V", photos))
    horizontal = filter(lambda item: item[1] == "H", photos)
    horizontal = list(map(lambda item: ((item[0], ),) + item[1:], horizontal))
    averageH = pairing.findHAverage(horizontal)

    vertical = pairing.pair(vertical, averageH)

    photos = sorting.sort(vertical + horizontal)

    #score.check_nearby(photos)

    slides = convert_to_slides(photos)

    #random.shuffle(slides)
    print("Started write")
    file_io.write_output(dataset, slides)
    print("finished dataset " + dataset)

print("done")