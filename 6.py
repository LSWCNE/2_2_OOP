a: None = None

# Callable(param...) -> return tpye
def sum(x: int, y: int) -> int:
    return x + y

class Bar:
    def __init__(self, x: int, y: str) -> None:
        self.x:int = x
        self.y:str = y
        