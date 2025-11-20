from typing import Any, Self

def out_func():
    def in_func(id:int):
        print(f"in_func: id -> {id}")
        
    return in_func

my_func_1 = out_func()

my_func_1(1)
my_func_1(2)

