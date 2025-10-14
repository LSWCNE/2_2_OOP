# 추상화 (Abstract) -> OOP
# 미완성 + 강제 구현

class Bar:
    # 반드시 자식 클래스에서 구현되기를 바란다.
    def test(self):
        raise NotImplementedError
    
class Foo(Bar):
    ...
    
obj = Foo() # -> Ok
obj.test()