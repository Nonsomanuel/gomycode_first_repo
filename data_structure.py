# student = ['Jack', 32, 'Computer Science', [2, 4], 4.29, True]
# print(student[2:4])

# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# print('original list:', fruits)
#
# fruits.append('Pineapple')
# print('Updated list:' , fruits)
#
# fruits.insert(2, 'Mango')
# print('Latest updated list' , fruits)
#
# #Joining two lists
# numbers = [1, 3, 5]
# print('Numbers:', numbers)
# even_numbers  = [2, 4, 6]
# print('Even numbers:', even_numbers)
# # adding elements of one list to another
# numbers.extend(even_numbers)
# print('Updated Numbers:', numbers)
#
# num = [1, 2, 3, 4, 5]
# print('Num:', num)
# oddNumbers = [3, 7, 9]
# print('Odd numbers:', oddNumbers)
# # add both elements
# num.extend(oddNumbers)
# print('Updated Num:', num)
#
# #Removing elements from list
# num.remove(3)
# print('Updated Num:', num)
#
# del num[1:3]
# print(num)
#
# print('Odd numbers list:' , len(oddNumbers))

# list = [17, 38, 10, 25, 72]
# print('Original list:', list)
#
# # list.insert(2, 12)
# list.append(12)
# print('Updated list:', list)

# list.reverse()
# # reversed_list = list[::-1]
# print('Reversed list:', list)

# index = list.index(17)
# print('Index of 17:', index)
#
# list.remove(38)
# print('Updated list after removing 38:', list)

#Dictionary
# student = {
#     "name": 'Victor',
#     "age": 20,
#     "Department": 'Data Science',
#     "courses": ['Python', 'Data Analysis', 'Machine Learning'],
#     "reg_number": "2026GMYC234",
# }
# print('Student Information:', student)
# # # print('Student Name: ', student['name'])
# # # print('Student Department: ', student['Department'])
# #
# student['GPA'] = "4.0"
# print('Updated Student Information:', student)

# del student['age']
# print('Updated Student Information after removing age:', student)

# student.clear()
# print('Student Information after clearing:', student)

# #Updating my dictionary
# student['GPA'] = "2.5"
# print('Updated Student Information after changing GPA:', student)
#
# print(len(student))
# print("Department" in student)
# print("Lecturer" in student)

# Sets in Python
mySet = {101, 102, 103, 104, 105}
print('My Set:', mySet)

mixed_set = {1, 2, 3, 'Ayo', 'Victor', 10.25, 20.50, 2, 3, 3, 2}
print('Mixed Set:', mixed_set)

mixed_set.add('Lekan')
print('Updated Mixed Set:', mixed_set)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

mixed_set.update(fruits, mySet)
print('Updated Mixed Set with Fruits:', mixed_set)

setSum = sum(mySet)
print('Sum of mySet:', setSum)

#Tuples in Python
myTuple = (1, 2, 3, 4, 5)
print('My Tuple:', myTuple)

print('First Element of myTuple:', myTuple[0])