# class Bar:
#     cValue = 100
    
#     def i_method(self):
#         self.iValue = 20
        
#     @classmethod
#     def c_method(cls):
#         cls.cValue = 30
        
# obj = Bar()
# obj.i_method()
# Bar.c_method()
# del obj.iValue
# del Bar.cValue
# del Bar.i_method
# Bar.cValue = 1000

class Bar:
    
    def __init__(self, id):
        self.id = id
        print(f"constructor of object {self.id} is invoked")
    
    def __del__ (self):
        print(f"destructor of object {self.id} is invoked")
        
obj1 = Bar(1)
obj2 = Bar(2)
del obj1
print("Program is terminated")
del obj2