#First Class Functions are those functions which returns value as functions as well as can pass function as an argument which treats function as an entity
#Example 1:
def sum(x,y):
    return x+y

SumOfTwoNums = sum
print(SumOfTwoNums.__name__)
num1 = 3
num2 = 4
result = SumOfTwoNums(num1,num2)
print(f"Sum of {num1} and {num2} :",result)

#Example 2 :
def square(x):
    return x*x


def my_map(func,lst):
    square_list = []
    for i in lst:
        square_list.append(func(i))
    return square_list

list1 = [2,4,5,7,8]
square_list = my_map(square,list1)
print(f"The square list : {square_list}")
