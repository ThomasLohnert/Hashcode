def pair(vert_photos, averageH):
    """
    Takes a list of vertical photos and returns a paired list
    :param photos: list[tuple] : [(idn, orientation, num_of_tags, tags)]
    :return: list[((),())] [((idn, orientation, num_of_tags, tags), (idn, orientation, num_of_tags, tags))]
    """

    out = []

    while vert_photos:
        first = vert_photos.pop()
        best = (100000000000, None)
        for second in vert_photos:
            paired = pair_single(first, second)
            sum = paired[2]
            if abs(sum-averageH) < best[0]:
                best = (sum-averageH, paired, second)
        vert_photos.remove(best[2])
        out.append(best[1])

    return out

def pair_single(p1,p2):
    #((id1,id2),v,tags
    tags = list(set().union(p1[3], p2[3]))
    return (p1[0], p2[0]), "V", len(tags), tags

def findHAverage(horiz_photos):
    total = 0
    for p in horiz_photos:
        total +=p[2]
    return total/len(horiz_photos)
