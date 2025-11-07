class Student:
    def __init__(self, id:int) -> None:
        self.id: int = id
        self.kor:int = 0
        self.eng:int = 0
        self.math:int = 0

    def __call__(self, kor:int, eng:int, math:int):
        self.kor = kor
        self.eng = eng
        self.math = math
    
    def __str__(self):
        return f"Kor: {self.kor}, Eng: {self.eng}, Math: {self.math}"
    
    def __eq__(self, value: "Student") -> bool:
        return self.id == value.id

obj = Student(1)
obj(10, 20, 30)

print(obj)        