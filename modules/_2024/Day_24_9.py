from typing import Tuple


def main(input_string: str) -> Tuple[int, int]:
    """Calculate the checksum of a compacted disk and return it.
    """
    disk = list()
    idx = 0
    checksum = 0

    # Precompute values to reduce redundant calculations
    last_current_id = (len(input_string) - 1) // 2
    max_length_compacted_disk = sum(int(bit) for bit in input_string[0::2])
    length_compacted_disk = 0
    current_last_bit_remaining = int(input_string[last_current_id * 2])

    # Main loop to fill the compacted disk and calculate checksum
    while length_compacted_disk < max_length_compacted_disk:
        actual_bit = int(input_string[idx])

        # Handle even indices (direct placement of bits)
        if idx % 2 == 0:
            add_length = min(max_length_compacted_disk -
                             length_compacted_disk, actual_bit)
            for _ in range(add_length):
                checksum += length_compacted_disk * (idx // 2)
                length_compacted_disk += 1
            idx += 1

        # Handle odd indices (fill from the back)
        else:
            free_space_filled = 0
            while free_space_filled < actual_bit and length_compacted_disk < max_length_compacted_disk:
                # Fill from the last current id's remaining bits
                fillable = min(current_last_bit_remaining,
                               actual_bit - free_space_filled)
                for _ in range(fillable):
                    checksum += length_compacted_disk * last_current_id
                    length_compacted_disk += 1
                    free_space_filled += 1
                    current_last_bit_remaining -= 1

                # If the current_last_bit_remaining is exhausted, move to the next
                if current_last_bit_remaining == 0 and last_current_id > 0:
                    last_current_id -= 1
                    current_last_bit_remaining = int(
                        input_string[last_current_id * 2])

            idx += 1

    return checksum, 'Not yet solved'
