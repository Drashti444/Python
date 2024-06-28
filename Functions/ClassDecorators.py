class Decorator_class:

  def __init__(self,func):
    self.originalFunc = func
    print("Insid __init__ ")


  def __call__(self,*args,**kwargs):
    print("Insid __call__ func.__name__: ",self.originalFunc.__name__)
    return self.originalFunc(*args, **kwargs)


@Decorator_class
def display():
    print("Hello, Good Morning!")

@Decorator_class
def display_name(name,greetings):
    print(f"Hello {name}, {greetings}")

# f1 = Decorator_class(display)
# print(f1.__name__)
# f1
#
# f2 = Decorator_class(display_name)
# print(f2.__name__)
# f2("Drashti","Good Morning!")

display()
display_name("Drashti","Good Morning!")
