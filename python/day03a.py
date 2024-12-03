import io
import re
import os

EXAMPLE_INPUT = (
    """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
)
EXAMPLE_OUTPUT = 161


MUL_RE = re.compile(r"mul\((?P<x>\d+),(?P<y>\d+)\)")


def solve(input: str) -> int:
    return sum(int(m['x']) * int(m['y']) for m in MUL_RE.finditer(input))


assert solve(EXAMPLE_INPUT) == EXAMPLE_OUTPUT


def main():
    prefix = os.path.splitext(os.path.basename(__file__))[0][:-1]
    with open(f"input/{prefix}.txt") as file:
        solution = solve(file.read())
        print(solution)


if __name__ == "__main__":
    main()
