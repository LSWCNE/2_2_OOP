class Parent:
    def __init__(self):
        self.name = "Parent"
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name = "Child"
        
print(Child, __bases__)