from typing import Tuple
from collections import defaultdict
from itertools import combinations
from modules.common import pos_in_grid


def main(inputs: str) -> Tuple[int, int]:
    # Convert input into a grid (list of strings)
    grid, nb_row, nb_col = inputs.splitlines()

    # Using defaultdict to store antennas' positions grouped by their type
    antennas = defaultdict(list)

    # Populate the antennas dictionary with positions of non-empty grid cells
    for y in range(nb_row):
        for x in range(nb_col):
            if grid[y][x] != '.':
                antennas[grid[y][x]].append((x, y))

    # Initialize sets to track unique and all antinode positions
    antinodes = set()
    res_antinodes = set()

    # Iterate over all antenna types and their respective positions
    for _, pos in antennas.items():
        # Generate all combinations of two distinct positions
        for pt1, pt2 in combinations(pos, 2):
            # Calculate the vector between points
            dx, dy = pt2[0] - pt1[0], pt2[1] - pt1[1]
            vectors = ((-dx, -dy), (dx, dy))  # Two opposite direction vectors

            # Iterate over each vector and point to generate possible antinode positions
            for vector, point in zip(vectors, (pt1, pt2)):
                antinode = point
                count = 0

                # Traverse in the direction of the vector and track positions
                while pos_in_grid(*antinode, nb_row, nb_col):
                    if count == 1:  # Add the first valid antinode to the set
                        antinodes.add(antinode)
                    res_antinodes.add(antinode)
                    # Move to the next position
                    antinode = (antinode[0] + vector[0],
                                antinode[1] + vector[1])
                    count += 1

    # Return the number of unique antinode positions and total antinode positions found
    return len(antinodes), len(res_antinodes)
