class  Foo:
    univ = "YJU"
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def prt_info(self):
        self.age = 20
        print(self.id, self.name, self.age)
        
obj = Foo()
obj.prt_info()