class Foo:
    name = "사람"
    
    def __init__(self, name):
        self.name = name
        
obj = Foo("Hong")


print(obj.name)