import io
import os

EXAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""
EXAMPLE_OUTPUT = 11


def solve(reader: io.TextIOBase) -> int:
    xs = list[int]()
    ys = list[int]()
    for line in reader:
        [x, y] = line.rstrip().split()
        xs.append(int(x))
        ys.append(int(y))
    return sum(abs(x - y) for x, y in zip(sorted(xs), sorted(ys)))


assert solve(io.StringIO(EXAMPLE_INPUT)) == EXAMPLE_OUTPUT


def main():
    prefix = os.path.splitext(os.path.basename(__file__))[0][:-1]
    with open(f"input/{prefix}.txt") as file:
        solution = solve(file)
        print(solution)


if __name__ == "__main__":
    main()
