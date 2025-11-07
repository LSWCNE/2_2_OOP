class MyData:
    def __init__(self, data: list) -> None:
        self.data: list = data
    
    def __iter__(self):
        return iter(self.data)
    
    def __next__(self) -> int:
        return 1
        
data = MyData([1, 2, 3, 4, 5])

for x in data:
    print(x)