
from typing import Any

class Module:
    def __init__(self, input: int, output: int) -> None:
        
        self.weight = [random.gauss(0, 1) for _ in range(input)]
        self.bias = [random.gauss(0, 1) for _ in range(output)]
    
    
module = Module(3, 1)

for w, b in module.parameters():
    print(w, b)