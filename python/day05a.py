import io
import os
from itertools import takewhile

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
EXAMPLE_OUTPUT = 143


def solve(reader: io.TextIOBase) -> int:
    result = 0
    lines = iter(map(str.rstrip, reader))
    rules = dict[int, set[int]]()
    for rule in takewhile(bool, lines):
        [lhs, rhs] = rule.split("|")
        rules.setdefault(int(lhs), set()).add(int(rhs))

    for update in lines:
        pages = [int(u) for u in update.split(",")]
        seen = set[int]()
        for page in pages:
            if not rules.get(page, set()).isdisjoint(seen):
                break
            seen.add(page)
        else:
            result += pages[len(pages) // 2]
    return result


assert solve(io.StringIO(EXAMPLE_INPUT)) == EXAMPLE_OUTPUT


def main():
    prefix = os.path.splitext(os.path.basename(__file__))[0][:-1]
    with open(f"input/{prefix}.txt") as file:
        solution = solve(file)
        print(solution)


if __name__ == "__main__":
    main()
