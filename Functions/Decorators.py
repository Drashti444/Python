def Decorator_func(func):
    def wrapper_func():
        return func()
    return wrapper_func

@Decorator_func
def display():
    print("Good Morning!")

f1 = Decorator_func(display)
print(f1.__name__)
f1()

display()
