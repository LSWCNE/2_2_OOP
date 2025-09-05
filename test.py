class Foo:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_name(self, name):
        self.name = name
        
    def set_age(self, age):
        self.age = age
    
obj = Foo()
obj.set_name("Hong")
print(obj.name)

del obj.name
print(obj.name)
    
        
#     name = "Class member variable: Foo"
#     # 생성자
#     # 멤버 속성   
#     def test (ibstance_ref):
#         ibstance_ref.name = "Instance member variable: Foo"
                
# obj = Foo()
# obj.test()

# print(obj.name)