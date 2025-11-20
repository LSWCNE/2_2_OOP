from typing import Any, Self

def test(func):
    print("test")
    
@test # 인퍼트리터가 코드 해석 시 해당 함수(메서드) 호출한다.
def bar():
    print("bar")
    
@test
def foo():
    print("foo") 