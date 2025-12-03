from typing import Tuple
from collections import defaultdict


def main(inputs: str) -> Tuple[int, int]:
    # Split the inputs into rules and update sections
    rules, updates = inputs.split('\n\n')

    # Parse and store the rules in a defaultdict
    # Each rule maps an antecedent page to a list of successor pages
    print_order = defaultdict(list)
    for rule in rules.splitlines():
        ant, succ = map(int, rule.split("|"))
        print_order[ant].append(succ)

    # Initialize solutions
    sol1, sol2 = 0, 0

    # Process each update
    for update in updates.splitlines():
        # Parse the pages in the update
        pages = list(map(int, update.split(",")))

        def count_successors(page: int) -> int:
            # Count the number of successors of the given page present in the update.
            return sum(1 for succ in print_order[page] if succ in pages)

        # Sort pages by the number of successors in descending order
        sorted_pages = sorted(pages, reverse=True, key=count_successors)

        # Check if the sorted order matches the original update
        # Add the middle element of the update or sorted update to the respective solution
        mid_index = len(pages) // 2
        if sorted_pages == pages:
            sol1 += pages[mid_index]
        else:
            sol2 += sorted_pages[mid_index]

    return sol1, sol2
