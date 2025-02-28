
from invert_dict import invert_dict
# from icecream import ic

data = {'a': set(['aa']),
        'b': set(['b1', 'b2']),
        'c': set(['aa', 'b1'])}


# def invert_dict(d: dict[str, set[str]]) -> dict[str, set[str]]:
#     inverted: dict[str, set[str]] = defaultdict(set)
#     for (key, value_set) in d.items():

#         for element in value_set:
#             inverted[element].add(key)

#     return dict(inverted)


def test_invert_dict():
    assert invert_dict(invert_dict(data)) == data


if __name__ == '__main__':
    invert_dict(data)
