# Union -> 집합의 원소 중 하나이면 -> Ok, 모두 해당되지 않으면 -> Error

# Optional -> if else -> if [T] else None

from typing import Callable

def sum(x: float, y: float) -> float:
    return x + y

sum_2 = sum
print(sum_2(2, 3))

def do_something(x: float, y: float, op: Callable[[매개변수], [반환형]]):
    return op(x, y)

do_something(1, 2, sum)