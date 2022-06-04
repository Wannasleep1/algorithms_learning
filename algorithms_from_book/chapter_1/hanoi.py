from typing import TypeVar, Generic, List

T = TypeVar("T")


class Stack(Generic[T]):

    def __init__(self, name) -> None:
        self._container: List[T] = []
        self.name = name

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


# Towers
num_discs: int = 3
tower_a: Stack[int] = Stack("A")
tower_b: Stack[int] = Stack("B")
tower_c: Stack[int] = Stack("C")
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        print("Move disk 1 from disk", begin.name, "to disk", end.name)
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        print("Move disk", n, "from disk", begin.name, "to disk", end.name)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)
        print("Move disk", n, "from disk", begin.name, "to disk", end.name)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
