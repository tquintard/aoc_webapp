from typing import Tuple
import re
from math import prod

OPS = [prod, sum, lambda x: int(str(x[0])+str(x[1]))]


def is_valid_eq(result, operands, part) -> bool:
    """
    Recursively checks if the operands can be combined using the allowed 
    operations up to the given part to produce the target result.
    """
    # Base case: If only one operand is left, check if it matches the result
    if len(operands) == 1:
        return operands[0] == result
    # Try all operations from OPS up to the given part
    for op in OPS[:part+1]:
        # Apply the operation on the first two operands and recurse
        if is_valid_eq(result, [op(operands[:2])] + operands[2:], part):
            return True
    # If no operation leads to the result, return False
    return False


def main(inputs: str) -> Tuple[int, int]:
    """
    Processes a series of equations and calculates the sum of results for 
    which the operands can be combined to match the result using 
    different subsets of operations.
    """

    equations = inputs.splitlines()
    sol = [0, 0]
    for eq in equations:
        # Parse the result and operands from the equation
        result, *operands = map(int, re.findall(r"(\d+)", eq))
        # Evaluate for each part (1 and 2) and add to the corresponding sum
        for part in (1, 2):
            sol[part -
                1] += result if is_valid_eq(result, operands, part) else 0
    return tuple(sol)
