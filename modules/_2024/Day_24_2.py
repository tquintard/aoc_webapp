from typing import List, Tuple
import numpy as np


def report_is_safe(report: List[int]) -> bool:
    # Calculate the sign of the first difference
    sign = np.sign(report[1] - report[0])

    # Pair consecutive elements using zip
    zipped_report = zip(report[:-1], report[1:])

    # Check the safety conditions for all pairs
    return all(
        np.sign(b - a) == sign and 1 <= abs(b - a) <= 3
        for a, b in zipped_report
    )


def main(inputs: str) -> Tuple[int, int]:
    # Parse and organize input data into a list of reports
    reports = [list(map(int, report.split()))
               for report in inputs.splitlines()]

    # Initialize counters for safe and fixable reports
    safe_reports = 0
    fixable_reports = 0

    # Evaluate each report
    for report in reports:
        if report_is_safe(report):
            safe_reports += 1
        else:
            # Check if the report can be fixed by removing one element
            for idx in range(len(report)):
                # Remove the element at the current index and check safety
                if report_is_safe(report[:idx] + report[idx+1:]):
                    fixable_reports += 1
                    break

    return safe_reports, safe_reports + fixable_reports
