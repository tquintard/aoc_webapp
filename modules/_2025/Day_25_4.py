from collections import defaultdict
from typing import DefaultDict, Set, Tuple

from modules.common import FULL_LOOK_DIR, next_position


def main(inputs: str) -> tuple[int, int]:
    # Map each character to the set of positions where it appears.
    char_loc: DefaultDict[str, Set[Tuple[int, int]]] = defaultdict(set)
    for y, line in enumerate(inputs.splitlines()):
        for x, char in enumerate(line):
            char_loc[char].add((x, y))

    nb_accessible_rolls: list[int] = []

    # Iteratively remove rolls that are not surrounded by 4 roll neighbors.
    while True:
        rolls_to_collect: Set[Tuple[int, int]] = set()
        for roll_pos in char_loc["@"]:
            neighbors_pos = get_neighbors_pos(roll_pos)
            if len(neighbors_pos & char_loc["@"]) < 4:
                rolls_to_collect.add(roll_pos)

        if len(rolls_to_collect) == 0:
            break

        char_loc["@"].difference_update(rolls_to_collect)
        nb_accessible_rolls.append(len(rolls_to_collect))

    return nb_accessible_rolls[0], sum(nb_accessible_rolls)


def get_neighbors_pos(pos: Tuple[int, int]) -> Set[Tuple[int, int]]:
    """
    Compute the neighbor positions of a given cell.

    The neighbors are obtained by applying each direction in FULL_LOOK_DIR
    through the ``next_position`` helper.

    Args:
        pos: The (x, y) coordinate of the reference cell.

    Returns:
        A set of (x, y) coordinates corresponding to the neighboring positions.
    """
    neighbours: Set[Tuple[int, int]] = set()
    for direction in FULL_LOOK_DIR:
        neighbours.add(tuple(next_position(pos, direction)))
    return neighbours



SAMPLE = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.\
"""
