from dataclasses import dataclass




@dataclass
class Student:
    id:str
    name:str
    age:int
    
std1 = Student("123", "kim", 20)
std2 = Student("124", "Lee", 30)

print(std1)
print(std2.name, std2.id, std2.age)