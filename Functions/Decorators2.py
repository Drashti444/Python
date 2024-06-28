def Decorator_func(func):
    print(f"Inside Decorator_func: func.__name__:", func.__name__)
    def wrapper_func(*args,**kwargs):
        print(f"Inside wrapper_func: func.__name__:",func.__name__)
        return func(*args,**kwargs)
    return wrapper_func

@Decorator_func
def display():
    print("Hello, Good Morning!")

@Decorator_func
def display_name(name,greetings):
    print(f"Hello {name}, {greetings}")

f1 = Decorator_func(display)
print(f1.__name__)
f1()

f2 = Decorator_func(display_name)
print(f2.__name__)
f2("Drashti","Good Morning!")

display()
display_name("Drashti","Good Morning!")
