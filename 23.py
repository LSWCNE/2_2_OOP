
def is_login(func):
    def wrapper(msg:str):
        func(msg)
        
    return wrapper

@is_login 
def do_something(msg:str):
    print(f"do something: {msg}")
    
do_something("h1")
do_something("h2")