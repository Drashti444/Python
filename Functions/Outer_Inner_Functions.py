def outer():
  print("Outer function starts------")
  def inner():
    print("Inner function starts------")
    print("Inner function ends!!!!!!!!!")
    return True
  print("End of Outer function!!!!!!!!!!!")
  return inner

f1 = outer()
print(f1)
print("Type of f1:",type(f1))
value = f1()
print("Return value of f1:",value)
f2 = outer
print(f2)
print("Type of f2:", type(f2))
f3 = f2()
h1 = f3()
print(h1)
