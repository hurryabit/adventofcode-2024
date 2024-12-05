import io
import os
from itertools import takewhile
from typing import Self

EXAMPLE_INPUT = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
EXAMPLE_OUTPUT = 123


def solve(reader: io.TextIOBase) -> int:
    result = 0
    lines = iter(map(str.rstrip, reader))
    rules = dict[int, set[int]]()
    for rule in takewhile(bool, lines):
        [lhs, rhs] = rule.split("|")
        rules.setdefault(int(lhs), set()).add(int(rhs))

    class Page:
        def __init__(self, num: str) -> None:
            self.num = int(num)

        def __eq__(self, other: object) -> bool:
            return isinstance(other, Page) and self.num == other.num

        def __lt__(self, other: Self) -> bool:
            return other.num in rules.get(self.num, set())

    for update in lines:
        pages = [Page(u) for u in update.split(",")]
        right = pages.copy()
        right.sort()
        if right != pages:
            result += right[len(right) // 2].num
    return result


assert solve(io.StringIO(EXAMPLE_INPUT)) == EXAMPLE_OUTPUT


def main():
    prefix = os.path.splitext(os.path.basename(__file__))[0][:-1]
    with open(f"input/{prefix}.txt") as file:
        solution = solve(file)
        print(solution)


if __name__ == "__main__":
    main()
