# Iteration: 순회
# 순차적으로 값을 꺼내오는 방법
# 처음부터 마지막까지 하나씩 꺼내오는 방법
# collection 자료형에서 주로 사용

# x = [_ for _ in range(10) ]

# for v in x:
#     print(v)
    
    
# collection이란? -> 자료구조를 담고 있는 프레임워크
# list, tuple, set, dict, str
from typing import Sequence

class Bar:
    def __init__(self, data: Sequence[int]) -> None:
        self.data:Sequence = data
        
    # iterable 객체가 되기 위한 조건
    # iterator가 하는 역할: 순회할 수 있도록 정의
    def __iter__(self):
        return BarIterator(self.data)
    
class BarIterator:
    def __init__(self, data:Sequence) -> None:
        self.data:Sequence = data
        self.index:int = 0
        
    # next 메서드: 순회할 때마다 호출되는 메서드
    def __next__(self):
        # self.data 리스트의 0번째 요소에서 마지막 요소까지 순회
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        
        raise StopIteration
    
obj = Bar([1, 2, 3, 4])

for v in obj:
    print(v)
    
for v in obj:  # index 인스턴스 변수는 이미 4가 되어있음
    print(v)   # 그래서 아무것도 출력되지 않음