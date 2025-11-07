from typing import Any



class Bar:
    def __init__(self) -> None:
        self.name = "Bar" # name: name, value: Bar

    # event -> 객체 멤버 변수에 값을 넣을 때    
    def __setattr__(self, name: str, value: Any) -> None:
        object.__setattr__(self, name, value)
        print(f"name: {name}, value: {value}")
        
    def __getattribute__(self, name: str) -> Any:
        try:
            value = object.__getattribute__(self, name)
            print(f"Get: {value}")
            return value
        except AttributeError:
            print(f"MISSING: {name}")

obj = Bar() 
# obj.bar -> 존재하지 않는다

obj.bar = 3 # name: bar, value: 3

# obj.bar ? 존재하지 않는다
print(obj.bar) # No attribute