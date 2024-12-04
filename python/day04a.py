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
EXAMPLE_OUTPUT = 18


def solve(reader: io.TextIOBase) -> int:
    map = StrMap.from_textio(reader)
    return sum(
        1
        for pos in map
        for dir in Pos.DIRS8
        if all(
            (p := pos + i * dir) in map and map[p] == x for i, x in enumerate("XMAS")
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
