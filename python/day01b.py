import io
import os
from collections import Counter

EXAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""
EXAMPLE_OUTPUT = 31


def solve(reader: io.TextIOBase) -> int:
    xs = list[int]()
    ys = Counter[int]()
    for line in reader:
        [x, y] = line.rstrip().split()
        xs.append(int(x))
        ys[int(y)] += 1
    return sum(x * ys[x] for x in xs)


assert solve(io.StringIO(EXAMPLE_INPUT)) == EXAMPLE_OUTPUT


def main():
    prefix = os.path.splitext(os.path.basename(__file__))[0][:-1]
    with open(f"input/{prefix}.txt") as file:
        solution = solve(file)
        print(solution)


if __name__ == "__main__":
    main()
