from abc import ABC, abstractmethod

class Bar(ABC):
    
    # 추상 인스턴스 메서드 정의
    @abstractmethod
    def instance_method(self):
        pass
    
obj = Bar()