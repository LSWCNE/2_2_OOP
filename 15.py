def bar():...
def test():
    print("a")
    yield 1
    print("b")
    yield 2
    print("c")
    yield 3
    print("d")
    
obj = test()

print(obj.__next__())
print(obj.__next__())
print(obj.__next__())