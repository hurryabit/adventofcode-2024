import io
import os

from map import Pos, StrMap

EXAMPLE_INPUT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
EXAMPLE_OUTPUT = 9


NEEDLE = "XMAS"


def solve(reader: io.TextIOBase) -> int:
    map = StrMap.from_textio(reader)
    return sum(
        1
        for pos in map
        if (
            map[pos] == "A"
            and {map[p] for sign in [-1, 1] if (p := pos + sign * Pos(1, 1)) in map}
            == {"M", "S"}
            and {map[p] for sign in [-1, 1] if (p := pos + sign * Pos(1, -1)) in map}
            == {"M", "S"}
        )
    )


assert solve(io.StringIO(EXAMPLE_INPUT)) == EXAMPLE_OUTPUT


def main():
    prefix = os.path.splitext(os.path.basename(__file__))[0][:-1]
    with open(f"input/{prefix}.txt") as file:
        solution = solve(file)
        print(solution)


if __name__ == "__main__":
    main()
