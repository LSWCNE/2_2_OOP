from typing import Any, Self

class Bar:
    def __init__(self, name:str) -> None:
        self._name:str = name
        
    @property
    def name(self):
        return f"안녕하세요 {self._name}님"
    
    @name.setter
    def name(self, value:str):
        self._name:str = value
    
obj = Bar("YC Jung")
print(obj.name)