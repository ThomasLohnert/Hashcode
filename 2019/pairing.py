MAX_DIFF = 1.5

def pair(vert_photos, averageH):
    """
    Takes a list of vertical photos and returns a paired list
    :param photos: list[tuple] : [(idn, orientation, num_of_tags, tags)]
    :return: list[((),())] [((idn, orientation, num_of_tags, tags), (idn, orientation, num_of_tags, tags))]
    """

    out = []
    print("num of verts: {}".format(len(vert_photos)))

    print ("Av is {}".format(averageH))

    #vert_photos = sorted()

    while vert_photos:
        first = vert_photos.pop()
        best = (100000000000, None)
        for second in vert_photos:
            paired = pair_single(first, second)
            sum = paired[2]
            diff = abs(sum-averageH)
            if diff < MAX_DIFF*averageH:
                best = (sum - averageH, paired, second)
                break
            if diff < best[0]:
                best = (sum-averageH, paired, second)
        vert_photos.remove(best[2])
        out.append(best[1])

    print("Done verts")

    return out

def pair_single(p1,p2):
    #((id1,id2),v,tags
    tags = list(set().union(p1[3], p2[3]))
    return (p1[0], p2[0]), "V", len(tags), tags

def findHAverage(horiz_photos):

    total = 0
    for p in horiz_photos:
        total +=p[2]
    if len(horiz_photos):
        return total/len(horiz_photos)
    else:
        0
