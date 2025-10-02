from abc import ABC, abstractmethod

class Bar(ABC):
    
    # 추상 인스턴스 메서드 정의
    @abstractmethod
    def instance_method(self):
        pass
    
class MyClass(Bar):
    def instance_method(self):
        print("MyClass : instance_method")
        
obj = MyClass()
obj.instance_method()