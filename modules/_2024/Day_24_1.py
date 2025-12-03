from typing import Tuple
import re


def main(inputs: str) -> Tuple[int, int]:
    # Extract all integer values from the input list using regex
    all_locs = list(map(int, re.findall(r'(\d+)', inputs)))

    # Initialize r_loc and l_loc as separate lists
    r_loc, l_loc = list(), list()

    # Split all_locs into r_loc and l_loc by alternating indices
    for i in range(0, len(all_locs), 2):
        l_loc.append(all_locs[i]), r_loc.append(all_locs[i + 1])

    # Sort both location lists independently
    l_loc.sort(), r_loc.sort()

    # Calculate sol1: Sum of absolute differences between sorted locations
    sol1 = sum(abs(l - r) for l, r in zip(l_loc, r_loc))

    # Calculate sol2: Weighted sum based on occurrences
    sol2 = sum(l * r_loc.count(l) for l in l_loc)

    return sol1, sol2
