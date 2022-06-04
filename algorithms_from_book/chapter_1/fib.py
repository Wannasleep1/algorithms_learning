from functools import lru_cache
from typing import Dict, Generator


# Simple version
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2) if n > 1 else n


memo: Dict[int, int] = {0: 0, 1: 1}


# With simple memoization
def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]


# With auto-memoization
@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    return fib3(n - 1) + fib3(n - 2) if n > 1 else n


# Iterative implementation
def fib4(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next_: int = 1
    for _ in range(n-1):
        last, next_ = next_, last + next_
    return next_


# Same but generator
def fib5(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next_: int = 1
    for _ in range(n-1):
        last, next_ = next_, last + next_
        yield next_


if __name__ == "__main__":
    print(fib1(5))
    print(fib1(10))
    print("-" * 10)
    print(fib2(5))
    print(fib2(10))
    print("-" * 10)
    print(fib3(5))
    print(fib3(10))
    print("-" * 10)
    print(fib4(5))
    print(fib4(10))
    print("-" * 10)
    print([n for n in fib5(10)])
