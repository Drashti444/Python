import time
def Time_taken(func):
    def wrapper(*args,**kwargs):
        # print(f"{args}")
        start_time = time.time()
        # print(f"Start time: {start_time}")
        result = func(*args,**kwargs)
        # print(time.time())
        end_time = time.time()-start_time
        print(f"the factorial of {args} is {result}, and time taken for it is: {end_time}")
    return wrapper



#recursion funtion of factorial
def factorial(num):
    # print("Inside factorial")
    # print(num)
    if num == 1:
        return num
    else:
        return num * factorial(num-1)

#Factorial function using loop
@Time_taken
def Factorial(num):
    time.sleep(1)
    print("Inside Factorial")
    print(num)
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

num = 5
result = factorial(num)
print("Result of Recursion function:",result)
# Ans = Factorial(num)
# print(Ans)
Factorial(num)
