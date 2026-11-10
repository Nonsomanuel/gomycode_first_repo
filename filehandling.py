import numpy as np
import json
#Read mode in file handling

with  open('waris.txt', 'r') as file:
    content = file.read()
    # print(content)

#to read multiple lines in a file
# with open('waris.txt', 'r') as file:
#     for line in file:
#         print(line.strip())
#
# with open('Ayo.txt', 'w') as file:
#     file.write("Hello, My name is Ayo.\n")
#     file.write("I am a data science student in GoMyCode.\n")
#     file.write("I am interested in machine learning and artificial intelligence.\n")
#     # print("File written successfully.")

#Creating a new text file using an input from a user, using the input function in writemode
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# telephone = input("Enter your Phone numer: ")
# bvn = input("Enter your BVN: ")
# nin = input("Enter your NIN: ")
# address = input("Enter your home address: ")
# state = input("Enter your state of origin: ")
# with open('customer_info.txt', 'w') as file:
#     file.write(f"Name: {name}\n")
#     file.write(f"Age: {age}\n")
#     file.write(f"Phone Number: {telephone}\n")
#     file.write(f"BVN: {bvn}\n")
#     file.write(f"NIN: {nin}\n")
#     file.write(f"Address: {address}\n")
#     file.write(f"State of Origin: {state}\n")
#     print("Customer information written to file successfully.")

with open('customer_info.txt', 'r') as file:
    content = file.read()
    print(content)

# #Append mode in file handling
# with open('waris.txt', 'a') as file:
#     # file.write("\nWaris is a lazy student, but he is a good learner.")
#     # print(f'file appended successfully.')

with open('waris.txt', 'r') as file:
    content = file.read()
    # print(content)

#Using Numpy genfromtxt to read data from a text file
data = np.genfromtxt('student_performance_activity.csv', delimiter=',', dtype=None, names=True)
# print(data)

#Writing JSON data to a file
# data = {
#     "name": "Waris",
#     "age": 25,
#     "city": "Ilorin-West",
#     "country": "Nigeria"
#  }
# with open('data.json', 'w') as file:
#      json.dump(data, file)
#
# #Reading JSON data from a file
# with open('data.json', 'r') as file:
#     data = json.load(file)
#     print(data)
