from functools import reduce
from operator import add, mul
from modules.common import transpose

OP = {"*": mul, "+": add,}

def main(inputs: str) -> tuple[int, int]:
    sol1, sol2 = 0, 0
    lines = inputs.splitlines()

    # Last line contains all operators for the different problems
    last_line = lines[-1]

    # Compute indexes of each operator in the last line and add a sentinel
    op_indexes = sorted(
        [x for x, char in enumerate(last_line) if char in OP]
        + [len(last_line) + 1]
    )

    # Build the problem definition for each operator position
    problems = {
        idx: {
            "op": last_line[idx],
            "nb_digits": op_indexes[pos + 1] - idx - 1,
            "operands": [],
            "operands_transposed": [],
        }
        for pos, idx in enumerate(op_indexes[:-1])
    }

    # Extract operands for each problem from all lines except the operator line
    for line in lines[:-1]:
        for idx, problem in problems.items():
            nb_digits = problem["nb_digits"]
            operand = line[idx: idx + nb_digits]
            problem["operands"].append(operand)

    # Compute sol1 and sol2 for each problem
    for idx, problem in problems.items():
        # First aggregation: use operands as-is
        sol1 += reduce(OP[problem["op"]], map(int, problem["operands"]))

        # Second aggregation: transpose digits of operands to build new operands
        problem["operands_transposed"] = map(
                "".join,
                transpose(problem["operands"]),
        )

        sol2 += reduce(OP[problem["op"]], map(int, problem["operands_transposed"]))

    return sol1, sol2


SAMPLE = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  \
"""

