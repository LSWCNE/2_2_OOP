class Bar:
    name = "YC Jung"
    
    def __init__(self):
        self.age = 20
        
    def hello(self):
        print(self.name)
        
obj = Bar()
obj.hello()