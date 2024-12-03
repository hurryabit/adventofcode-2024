import io
import re
import os

EXAMPLE_INPUT = (
    """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
)
EXAMPLE_OUTPUT = 48

# https://pythex.org/?regex=mul%5C((%3FP%3Cmul_x%3E%5Cd%2B)%2C(%3FP%3Cmul_y%3E%5Cd%2B)%5C)%7C(%3FP%3Cdo%3Edo%5C(%5C))%7C(%3FP%3Cdont%3Edon%27t%5C(%5C))
OP_RE = re.compile(
    r"mul\((?P<mul_x>\d+),(?P<mul_y>\d+)\)|(?P<do>do\(\))|(?P<dont>don't\(\))"
)


def solve(input: str) -> int:
    do = True
    result = 0
    for m in OP_RE.finditer(input):
        match m.lastgroup:
            case "mul_y":
                if do:
                    result += int(m["mul_x"]) * int(m["mul_y"])
            case "do":
                do = True
            case "dont":
                do = False
            case _:
                raise Exception("IMPOSSIBLE")
    return result


assert solve(EXAMPLE_INPUT) == EXAMPLE_OUTPUT


def main():
    prefix = os.path.splitext(os.path.basename(__file__))[0][:-1]
    with open(f"input/{prefix}.txt") as file:
        solution = solve(file.read())
        print(solution)


if __name__ == "__main__":
    main()
