import re

RANGES: re.Pattern[str] = re.compile(r"(?:(?P<l_bound>\d+)-(?P<u_bound>\d+))")


def main(inputs: str) -> tuple[int, int]:
    sol1, sol2 = 0, 0

    # Split raw input into ranges block and IDs block.
    ranges_raw, ids_raw = inputs.split("\n\n")

    # Parse all ranges into (lower_bound, upper_bound) pairs.
    matches = re.finditer(RANGES, ranges_raw)
    ranges: list[tuple[int, int]] = []
    for match in matches:
        l_bound = int(match.group("l_bound"))
        u_bound = int(match.group("u_bound"))
        ranges.append((l_bound, u_bound))

    # Sort ranges by lower bound for subsequent merging.
    ranges = sorted(ranges, key=lambda x: x[0], reverse=False)

    # Merge overlapping ranges into an optimized list.
    ranges_optim: list[tuple[int, int]] = []
    idx = 0
    while idx < len(ranges) - 1:
        actual_range = ranges[idx]
        # Extend the current range while the next one overlaps it.
        while idx + 1 < len(ranges) and ranges[idx + 1][0] <= actual_range[1]:
            actual_range = (
                actual_range[0],
                max(actual_range[1], ranges[idx + 1][1]),
            )
            idx += 1
        ranges_optim.append(actual_range)
        idx += 1

    # Parse IDs into a sorted list of integers.
    ids: list[int] = sorted([int(x) for x in ids_raw.split("\n")])

    # For each merged range, count contained IDs and add range length.
    for r in ranges_optim:
        idx = 0
        # Skip IDs that are below the current range.
        while idx < len(ids) and ids[idx] < r[0]:
            idx += 1
        # Count IDs that lie inside the current range.
        while idx < len(ids) and ids[idx] <= r[1]:
            sol1 += 1
            idx += 1
        # Add the coverage length of the range.
        sol2 += r[1] - r[0] + 1

    return sol1, sol2




SAMPLE = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32\
"""
