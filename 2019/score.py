
def score_pair(left, right):
    _, _, _, left_tags = left
    _, _, _, right_tags = right
    left_tags = set(left_tags)
    right_tags = set(right_tags)
    intersection = left_tags.intersection(right_tags)
    l_diff = left_tags.difference(right_tags)
    r_diff = right_tags.difference(left_tags)
    return min([len(intersection), len(l_diff), len(r_diff)])

if __name__ == "__main__":
    a = (0, 'V', 3, ['dog', 'cat', 'turtle'])
    b = (0, 'V', 3, ['dog', 'cat', 'rabbit'])
    assert score_pair(a, b) == 1

    a = (0, 'V', 3, ['dog', 'cat', 'rabbit'])
    b = (0, 'V', 3, ['dog', 'cat', 'rabbit'])
    assert score_pair(a, b) == 0

    a = (0, 'V', 3, ['dog', 'cat', 'rabbit', 'hamster'])
    b = (0, 'V', 3, ['dog', 'cat', 'tom', 'dom'])
    assert score_pair(a, b) == 2