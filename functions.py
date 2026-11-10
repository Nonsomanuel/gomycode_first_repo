#Creating Functions in Python

# def square(number):
#     return number * number
#
# result = square(49)
# print(result)

#Greet function
# def greet(name):
#     return f"Hello, {name}, wishing you a great day ahead!"
#
# # greeting = greet("Alice")
# greeting = greet(input("Enter your name: "))
# print(greeting)

#Creating a Sum Function
# def add_numbers(num1, num2):
#     total = num1 + num2
#     return total
#
# # Example usage:
# sum_result = add_numbers(240, 119)
# print(sum_result)

#Creating a function with multiple parameters
# def operations(num1, num2, num3):
#     waris = (num1 + num2) / num3
#     return waris
# calculations = operations(20, 30, -5)
# print(calculations)

#Creating a function with default parameters
# def add_numbers(num1=5, num2=10):
#     total = num1 + num2
#     return total
#
#
# # default_result = add_numbers()
# # print(default_result)
#
# mynumbers = add_numbers(15, 25)
# print(mynumbers)

def test ():
    return test()
# print("this is a test function")

#Lambda function
# add = lambda x, y: x + y
# result = add(5, 10)
# # print(f'result: {result}')

#default function code
# def add (x, y):
#     return x + y
# result_def = add(5,10)
# # print(f'result_def: {result_def}')


#Map function
def get_length(word):
    return len(word)

fruits = ("apple", "banana", "cherry")

result = map(get_length, fruits)

print(f'result: {list(result)}')


datascienceAvengers = ["Victor", "Ayo", "Lekan", "Waris", "Elizabeth"]

avenger_lengths = list(map(get_length, datascienceAvengers))
print(f'avenger_lengths: {avenger_lengths}')

# print(len("Lekan"))
# print(len("Elizabeth"))

#Lambda + Map function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiples = lambda x: x * 2
result = list(map(multiples, numbers))
print(f'result: {result}')