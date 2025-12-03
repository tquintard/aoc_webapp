from modules.common import next_position, pos_in_grid, LOOK_DIR
from typing import Tuple, Set
from collections import defaultdict


def main(topo_map: str) -> Tuple[int, int]:
    """
    Analyse the topographic map to calculate:
    - The total number of unique "peak" positions (marked with a 9) reachable from a bottom position.
    - The total number of time peak are reachable from all bottom positions.
    """
    grid = []
    zero_positions = defaultdict(int)

    # Parse the map into a grid and locate all zero positions.
    for y, row in enumerate(topo_map.splitlines()):
        grid_row = []
        for x, col in enumerate(row):
            grid_row.append(int(col))
            if col == '0':
                zero_positions[(x, y)] = 0
        grid.append(grid_row)

    nb_row, nb_col = len(grid), len(grid[0])

    def check_next_pos(
        x: int, y: int, dx_dy: Tuple[int, int], act_height: int, top_pos: Set[Tuple[int, int]], counter: int
    ) -> Tuple[Set[Tuple[int, int]], int]:
        """
        Recursively checks the next positions in the grid to find the peaks (value 9).
        """
        if not pos_in_grid(x, y, nb_col, nb_row):
            return top_pos, counter

        if grid[y][x] == 9:
            top_pos.add((x, y))  # Set of all peak positions
            counter += 1  # Accumulate the number of time a peak is reachable
            return top_pos, counter

        for direction in LOOK_DIR:
            # Skip the check of the actual position
            if direction == (-dx_dy[0], -dx_dy[1]):
                continue
            next_x, next_y = next_position((x, y), direction)
            # Next position is in the grid and is one step higher
            if pos_in_grid(next_x, next_y, nb_col, nb_row) and grid[next_y][next_x] - act_height == 1:
                top_pos, counter = check_next_pos(
                    next_x, next_y, direction, grid[next_y][next_x], top_pos, counter
                )

        return top_pos, counter

    unque_peaks, acc_peaks_reach = 0, 0

    for (x, y) in zero_positions.keys():
        top_pos, counter = check_next_pos(x, y, (0, 0), grid[y][x], set(), 0)
        unque_peaks += len(top_pos)  # Count unique peak positions.
        acc_peaks_reach += counter  # Accumulate total steps to peaks.

    return unque_peaks, acc_peaks_reach
