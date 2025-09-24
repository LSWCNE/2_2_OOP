class Student:
    # 1. 클래스 속성
    count = 0  # 생성된 객체(학생)의 수

    # 2. 인스턴스 속성
    def __init__(self, student_id, name, eng, kor, math):
        Student.count += 1
        self.id = Student.count
        self.student_id = student_id
        self.name = name
        self.eng = eng
        self.kor = kor
        self.math = math
        self.total = 0
        self.average = 0.0

    # 3. 메서드
    # 합계 계산 메서드
    def calc_total(self):
        self.total = self.eng + self.kor + self.math
        return self.total

    # 평균 계산 메서드
    def calc_average(self):
        self.average = self.total/3

    # Getter/Setter 메서드
    def get_eng(self):
        return self.eng

    def set_eng(self, score):
        self.eng = score
        self.calc_total()
        self.calc_average()

    def get_kor(self):
        return self.kor

    def set_kor(self, score):
        self.kor = score
        self.calc_total()
        self.calc_average()

    def get_math(self):
        return self.math

    def set_math(self, score):
        self.math = score
        self.calc_total()
        self.calc_average()

# 학생 객체 생성        
s1 = Student("2025001", "kim", 90, 80, 85)
s2 = Student("2025002", "lee", 70, 75, 80)

s1.calc_total()
s1.calc_average()
s2.calc_total()
s2.calc_average()


# 결과 출력
print(s1.id, s1.name, s1.total, s1.average)
print(s2.id, s2.name, s2.total, s2.average)


# 학생 객체 개수 확인
print("총 학생 수:", Student.count)