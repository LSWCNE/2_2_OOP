




class MyDataset:
    def __init__(self, feature:list, label:list) -> None:
        self.feature: list = feature
        self.label: list = label
        
    def __str__(self):
        return (f"Dataset: \nfeatrue: {self.feature}\nlabel: {self.label}")

    def __repr__(self):
        return "For log, debuh and Doc"

    def __getitem__(self, index:int) -> tuple:
        return (self.feature[index], self.label[index])
    
    def __setitem__(self, index:int, value:tuple[list, list]) -> None:
        self.feature[index] = value[0]
        self.label[index] = value[1]
        
    def __len__(self):
        return len(self.feature)
    
    def __iter__(self):
        for x, y in zip(self.feature, self.label):
            yield x, y
            
dataset = MyDataset([1,2,3], [10,20,30])

for x, y in dataset:
    print("x, y:", x, y)
    
