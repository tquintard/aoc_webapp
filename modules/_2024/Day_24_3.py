from typing import Tuple
import re
from math import prod


def sum_valid_mul(code: str) -> int:
    """
    Calculates the sum of products for all 'mul(x, y)' patterns in the given code.
    """
    # Find all occurrences of 'mul(x, y)' and return as a list of digit tuples
    valid_mul = re.findall(r'mul\((\d+),(\d+)\)', code)

    # Convert the string digits to integers, calculate the product for each pair, and return the total sum
    return sum(prod(map(int, digits)) for digits in valid_mul)


def main(inputs: str) -> Tuple[int, int]:
    """
    Processes the input string to compute two sums:
    - sol1: Sum of products from all 'mul(x, y)' patterns in the input.
    - sol2: Sum of products from 'mul(x, y)' patterns after removing 
            "don't() ... do()" patterns.
    """
    # Remove newlines and spaces for easier processing with regex
    cleaned_code = inputs.replace("\n", "").replace(" ", "")

    # Compute the sum of products of all 'mul(x, y)' patterns in the cleaned input
    sol1 = sum_valid_mul(cleaned_code)

    # Remove all "don't ... do()" patterns from the input
    code_without_dont = re.sub(r"don't\(\).*?do\(\)", "", cleaned_code)

    # Compute the sum of products of 'mul(x, y)' patterns after removing "don't" patterns
    sol2 = sum_valid_mul(code_without_dont)

    # Return the two results as a tuple
    return sol1, sol2
