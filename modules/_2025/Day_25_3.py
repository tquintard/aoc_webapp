import re
import streamlit as st  # Unused import kept to avoid changing core structure.
from collections import defaultdict
import pandas as pd
IDS: re.Pattern[str] = re.compile(r"(?:(?P<first_id>\d+)-(?P<last_id>\d+)),?")


def main(inputs: str) -> tuple[int, int]:
    # Accumulators for the parts' solution.
    zoltage_power= {1:0, 11:0}
    for idx_lin, line in enumerate(inputs.splitlines()):
        len_line = len(line)
        for zoltage_len in zoltage_power.keys():
            next_id = 0           
            for power in range(zoltage_len, -1, -1):                               
                max_digit, next_id = find_next_digit(line, next_id, len_line - power)
                zoltage_power[zoltage_len] += max_digit * 10 ** power 
                
    return zoltage_power[1], zoltage_power[11]

def find_next_digit(line, idx_start, idx_end):
    max_digit = 0
    next_id = idx_start + 1
    for idx, digit in enumerate(line[idx_start:idx_end],start=idx_start):
        dig = int(digit)
        if dig == 9:
            return dig, idx + 1
        if dig > max_digit:
            max_digit = dig
            next_id = idx + 1
    return max_digit, next_id


SAMPLE = """\
987654321111111
811111111111119
234234234234278
818181911112111\
"""
