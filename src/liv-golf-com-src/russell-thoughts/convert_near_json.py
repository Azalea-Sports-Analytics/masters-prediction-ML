
import re


def extract_refs(raw: str) -> set[str]:
    return {match.group(1) for match in re.finditer(r'"\$([a-z0-9]+)"', raw)}




INFILE = "text-leader.txt"
# OUTFILE = "candidate.json"

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

    ranges: list[tuple[int, int]] = []
    with open(INFILE, 'r') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):

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


if __name__ == "__main__":
    main()
