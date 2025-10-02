from functools import singledispatch

@singledispatch
def bar(x):
    print("x")
    
