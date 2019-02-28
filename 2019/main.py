import file_io
import os
import sorting
import random
import pairing
import math
from score import *

DEBUG = True


def convert_to_slides(photos_tuples):
    out = []
    for photos in photos_tuples:
        out.append(photos[0])
    return out


def sequence(current_id, current_tags, remaining, sequenced):
    if len(remaining) > 0:
        match_id, match_tags = find_match(current_tags, remaining)
        sequenced.append(current_id)
        del remaining[match_id]
        return sequence(match_id, match_tags, remaining, sequenced)
    else:
        return sequenced


def find_match(current, remaining):
    max_score = 0
    match_id = None
    match_tags = []
    for slide_id, slide_tags in remaining.iteritems():
        slide_tags = slide_tags
        score = score_pair_tags_only(current, slide_tags)
        if score > max_score:
            match_id = slide_id
            match_tags = slide_tags
            max_score = score

    return match_id, match_tags


datasets = os.listdir("data")

for dataset in datasets:
    photos = file_io.read_input(dataset)

    vertical = list(filter(lambda item: item[1] == "V", photos))
    horizontal = filter(lambda item: item[1] == "H", photos)
    horizontal = list(map(lambda item: ((item[0], ),) + item[1:], horizontal))
    averageH = pairing.findHAverage(horizontal)

    vertical = pairing.pair(vertical, averageH)

    slides = sorting.sort(vertical + horizontal)

    first = slides[0]
    # (id1,id2),v,tags
    slide_dict = {}
    for slide in slides[1:]:
        slide_dict[slide[0]] = slide[3]

    print first
    sequenced_slides = sequence(first[0], first[3], slide_dict, [])
    print(sequenced_slides)
    #score.check_nearby(photos)

    #slides = convert_to_slides(photos)

    #random.shuffle(slides)
    print("Started write")
    file_io.write_output(dataset, slides)
    print("finished dataset " + dataset)

print("done")
