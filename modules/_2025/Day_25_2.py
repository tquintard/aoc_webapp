import re
import streamlit as st  # Unused import kept to avoid changing core structure.

IDS: re.Pattern[str] = re.compile(r"(?:(?P<first_id>\d+)-(?P<last_id>\d+)),?")


def main(inputs: str) -> tuple[int, int]:
    # Accumulators for the parts' solution.
    sol1: int = 0
    sol2: int = 0
    
    # Find all ID ranges in the input.
    matches = re.finditer(IDS, inputs)

    # For each range, try all possible invalid IDs.
    for match in matches:
        first_id_str, last_id_str = match.group("first_id"), match.group("last_id")
        len_last_id = len(last_id_str)
        first_id, last_id = int(first_id_str), int(last_id_str)
        potential_ids_invalid: set[int] = set()

        # Try all possible bases (number of repeated chunks) for this range.
        for base in range(2, len_last_id + 1):
            chunk_range: list[int | None] = []
            for _id in (first_id_str, last_id_str):
                chunk_range.append(get_first_chunk_value(str(_id), base))

            if chunk_range == [None, None]:
                continue

            full_range = refine_boundaries(*chunk_range, base, len_last_id)

            # Build candidate IDs by repeating each possible chunk "base" times.
            for chunk in range(*full_range):
                next_potential_id_invalid = int(str(chunk) * base)
                if first_id <= next_potential_id_invalid <= last_id:
                    potential_ids_invalid.add(next_potential_id_invalid)

        # Accumulate solutions based on collected invalid IDs.
        for invalid_id in potential_ids_invalid:
            sol2 += invalid_id
            invalid_id_str = str(invalid_id)
            invalid_id_len = len(invalid_id_str)

            # Check if the ID is exactly two identical halves.
            if invalid_id_str[: invalid_id_len // 2] == invalid_id_str[invalid_id_len // 2 :]:
                sol1 += invalid_id

    return sol1, sol2


def get_first_chunk_value(id_str: str, base: int) -> int | None:
    """
    Extract the first chunk value of an ID for a given base.

    The base represents the number of equal-sized chunks that compose the ID.
    If the length of the ID is not divisible by the base, the function returns
    None. Otherwise, the first chunk (as an integer) is returned.

    Args:
        id_str: String representation of the ID.
        base: Number of repeated chunks considered for this ID.

    Returns:
        The integer value of the first chunk if the ID can be split evenly
        into `base` chunks, otherwise None.
    """
    len_id_str = len(id_str)
    if len_id_str % base == 0:
        chunk_len_id = len_id_str // base
        chunks_id = [
            int(id_str[i : i + chunk_len_id])
            for i in range(0, len_id_str, chunk_len_id)
        ]
        return chunks_id[0]

    return None


def refine_boundaries(
    r_min: int | None,
    r_max: int | None,
    base: int,
    len_last_id: int,
) -> tuple[int, int]:
    """
    Normalize and refine the chunk boundaries used to generate candidate IDs.

    Args:
        r_min: Minimum chunk value or None if unspecified.
        r_max: Maximum chunk value or None if unspecified.
        base: Number of repeated chunks used to build each candidate ID.
        len_last_id: Number of digits of the upper bound ID in the current range.

    Returns:
        A tuple (r_min, r_max) representing the normalized half-open interval
        of chunk values to iterate over.
    """
    chunk_len_id = len_last_id // base
    if r_min is None:
        r_min = 10 ** (chunk_len_id - 1)
    if r_max is not None:
        r_max = r_max + 1
    else:
        r_max = 10 ** chunk_len_id
    return r_min, r_max


SAMPLE = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124\
"""
