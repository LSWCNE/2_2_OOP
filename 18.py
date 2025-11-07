from typing import Any, Self

class Bar:
    def __enter__(self) -> Self:
        print("Bar: enter")
        return self
    
    def div(self, x, y) -> float:
        return x / y
    
    def __exit__(self, exec_type, exec_value, traceback) -> bool:
        print(f"exit: type[{exec_type}], val: [{exec_value}], trace: [{traceback}]")
        return True
        
with Bar() as obj:
    obj.div(2, 0)