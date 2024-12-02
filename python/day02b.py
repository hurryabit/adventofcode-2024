import io
import os

EXAMPLE_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
EXAMPLE_OUTPUT = 4


def is_safe(report: list[int]) -> bool:
    diffs = [x - y for x, y in zip(report, report[1:])]
    diff0 = diffs[0]
    return all(1 <= abs(d) <= 3 and (d > 0) == (diff0 > 0) for d in diffs)


def is_dampened_safe(report: list[int]) -> bool:
    return is_safe(report) or any(
        is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))
    )


def solve(reader: io.TextIOBase) -> int:
    return sum(1 for line in reader if is_dampened_safe([int(x) for x in line.split()]))


assert solve(io.StringIO(EXAMPLE_INPUT)) == EXAMPLE_OUTPUT


def main():
    prefix = os.path.splitext(os.path.basename(__file__))[0][:-1]
    with open(f"input/{prefix}.txt") as file:
        solution = solve(file)
        print(solution)


if __name__ == "__main__":
    main()
