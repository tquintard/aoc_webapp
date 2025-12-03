from typing import List, Tuple

# Directions for neighbor look-up: up, right, down, left
LOOK_DIR = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# Directions to look for neighbors: right, diagonal-down-right, down, diagonal-down-left, left, diagonal-up-left, up, diagonal-up-right
FULL_LOOK_DIR = [(1, 0), (1, 1), (0, 1), (-1, 1),
                 (-1, 0), (-1, -1), (0, -1), (1, -1)]


def create_grid(inputs: List):
    grid = list()
    for line in inputs:
        grid.append(list(line))
    return grid, len(grid), len(grid[0])


def pos_in_grid(x: int, y: int, nb_col: int, nb_row: int) -> bool:
    """ Check if the position (x, y) is within the bounds of the grid """
    return 0 <= x < nb_col and 0 <= y < nb_row


def next_direction(current_dir: Tuple, directions: List[Tuple]) -> Tuple:
    """
    Get the next direction in a cyclic list of directions.
    """
    return directions[(directions.index(current_dir) + 1) % len(directions)]


def next_position(pos: Tuple[int, int], dx_dy: Tuple[int, int]) -> Tuple[int, int]:
    return map(sum, zip(pos, dx_dy))
