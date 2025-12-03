def main(inputs: str) -> tuple[int, int]:
    # Current position on the circular track [0, 99].
    pos: int = 50

    # Accumulators for the parts' solution.
    sol1: int = 0
    sol2: int = 0

    for line in inputs.splitlines():
        # Extract movement direction and distance from the current instruction.
        dir_mov: str = line[0]
        mov: int = int(line[1:])

        # Compute the next absolute position before wrapping on the circle.
        next_pos_abs: int = pos - mov if dir_mov == "L" else pos + mov

        # Wrap position on the interval [0, 99] to simulate circular movement.
        pos = next_pos_abs % 100

        # Count how many times the wrapped position is exactly 0.
        if pos == 0:
            sol1 += 1

        # Update the number of full laps crossed between positions.
        if dir_mov == "L":
            sol2 += pos // 100 - next_pos_abs // 100
        else:
            sol2 += next_pos_abs // 100 - pos // 100

    return sol1, sol2

def sample():
    return """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""