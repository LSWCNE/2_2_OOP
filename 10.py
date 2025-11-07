# Iteration : 순회
from re import S
from typing import Sequence

class Bar:
    def __init__(self, data: Sequence[int]) -> None:
        self.data:Sequence = data
        
    def __len__(self) -> int:
        return len(self.data)
    
obj = Bar([1, 2, 3, 4])

x = [10, 20, 30]

foo = iter(x)
while True:
    try:
        item = next(foo)
        print(item)
    except StopIteration:
        break
    