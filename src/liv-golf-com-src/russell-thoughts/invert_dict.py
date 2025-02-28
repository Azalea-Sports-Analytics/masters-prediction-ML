
from collections import defaultdict


def invert_dict(d: dict[str, set[str]]) -> dict[str, set[str]]:
    inverted: dict[str, set[str]] = defaultdict(set)
    for (key, value_set) in d.items():

        for element in value_set:
            inverted[element].add(key)

    return dict(inverted)
