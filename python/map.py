from __future__ import annotations
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from io import TextIOBase
from itertools import product
from typing import ClassVar, Final


@dataclass(frozen=True, order=True)
class Pos:
    row: int
    col: int

    DIRS8: ClassVar[Final[frozenset[Pos]]] = frozenset()

    def __add__(self, other: Pos) -> Pos:
        return Pos(self.row + other.row, self.col + other.col)

    def __neg__(self) -> Pos:
        return Pos(-self.row, -self.col)

    def __rmul__(self, scale: int) -> Pos:
        return Pos(scale * self.row, scale * self.col)


Pos.DIRS8 = frozenset(  # type: ignore
    Pos(row, col) for row, col in product([-1, 0, 1], repeat=2) if row != 0 or col != 0
)


class Map[T]:
    data: Sequence[Sequence[T]]

    def __init__(self, data: Sequence[Sequence[T]]) -> None:
        self.data = data

    def __iter__(self) -> Iterator[Pos]:
        for row, line in enumerate(self.data):
            for col in range(len(line)):
                yield Pos(row, col)

    def __contains__(self, pos: Pos) -> bool:
        return 0 <= pos.row < len(self.data) and 0 <= pos.col < len(self.data[pos.row])

    def __getitem__(self, pos: Pos) -> T:
        return self.data[pos.row][pos.col]


class StrMap(Map[str]):
    def __init__(self, data: Sequence[str]) -> None:
        super().__init__(data)

    @staticmethod
    def from_textio(reader: TextIOBase) -> StrMap:
        return StrMap([line.rstrip() for line in reader])
