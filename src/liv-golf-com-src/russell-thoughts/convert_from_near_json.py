import re
from invert_dict import invert_dict
from icecream import ic


# used for right hand side


def extract_refs(raw: str) -> set[str]:
    answer: set[str] = {match.group(
        1) for match in re.finditer(r'"\$([a-z0-9]+)"', raw)}
    return answer


INFILE = "text-leader.txt"
# OUTFILE = "candidate.json"

# used for left hand side
GOOD_RE = re.compile(
    r'^[0-9a-z]+:[{[]"'


)


def bad_line(line: str) -> bool:
    return not GOOD_RE.match(line)


def good_line(line: str) -> bool:
    return GOOD_RE.match(line) is not None


def main():
    bad_start: int = -1

    in_bad: bool = False

    children = dict[str, set[str]]()
    defined_on_line = dict[str, int]()

    ranges: list[tuple[int, int]] = []
    with open(INFILE, 'r') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):

            if good_line(line):
                my_label: str = line.split(":")[0]
                my_children: set[str] = extract_refs(line)
                # todo: check for collisions rather than just overwriting
                children[my_label] = my_children
                defined_on_line[my_label] = i
            if in_bad:
                if good_line(line):
                    in_bad = False
                    ranges.append((bad_start, i))
            else:
                # not in bad
                if bad_line(line):
                    in_bad = True
                    bad_start = i

    if in_bad:
        ranges.append((bad_start, len(lines)))
    if ranges:
        print("Bad Ranges:")
        for r in ranges:
            print(r)
    parents = invert_dict(children)

    ic(len(children), len(parents))
    print("\nKeys in children but not in parents:")
    for key in set(children) - set(parents):
        print(f'{key} defined on line {defined_on_line[key]}')
    # for symbol, my_children in children.items():
    #     print(f"{symbol} -> {my_children}")
    #     if not my_children:
    #         print(f"*** {defined_on_line[symbol]}:{symbol} is a leaf")
    # for symbol, in parents.items():
    #     print(f"{symbol} -> {my_parents}")
    #     if not my_parents:
    #         print(f"*** {defined_on_line[symbol]}:{symbol} is a root")


if __name__ == "__main__":
    main()
