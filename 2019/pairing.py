def pair(photos):
    """
    Takes a list of vertical photos and returns a paired list
    :param photos: list[tuple] : [(idn, orientation, num_of_tags, tags)]
    :return: list[(),()] [(idn, orientation, num_of_tags, tags), (idn, orientation, num_of_tags, tags)]
    """
    out = []
    last_vertical = None
    for p in photos:
        if last_vertical is None:
            last_vertical = p
        else:
            out.append((last_vertical, p))
            last_vertical = None

    return out