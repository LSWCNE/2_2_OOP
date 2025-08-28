class Bar:
    def prt_name(self):
        print("Bar")

class Foo:
    def prt_name(self):
        print("Foo")
        
bar_1 = Bar()
foo_1 = Foo()

def prt(obj):
    obj.prt_name()
    
prt(bar_1)
prt(foo_1)