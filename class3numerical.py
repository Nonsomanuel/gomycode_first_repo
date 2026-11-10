
import numpy as np

one_Dimensional_array = np.array([1, 2, 3, 4, 5])
print('1-Dimensional Array: ', one_Dimensional_array)

two_Dimensional_array = np.array([[1, 2, 3], [4, 5, 6]])
print('2-Dimensional Array: ', two_Dimensional_array)
print(two_Dimensional_array.shape)

#Reshaping in Python
a = np.array([1,0,1,0,2,0,2,0])
print('Reshape_Array: ', a.reshape(2,4))
#
# print(two_Dimensional_array[1,2])
# print(one_Dimensional_array[:4])

#Random numbers in Python
value1 = np.random.random((3, 4))
print('Random Value: ', value1)

#Random whole numbers (integers) in python
value2 = np.random.randint(1, 20, size=(3, 4))
print('Random Integer: ', value2)

#Random student scores
score = np.random.randint(20, 100, size=(10,))
print('Student Scores: ', score)

#Creating an array of Zeros
zero_array = np.zeros((3,3))
print(zero_array)

#Creating an array of Ones
one_array = np.ones(4)
print(one_array)

#Creating an array of a specific value
# specific_value = np.full((5, 4), 8)
# print(specific_value)
#
# #Eye function in python
# eye_array = np.eye(4)
# print(eye_array)

#Numpy data types
z = np.array(
    [[1,2],[3,4]],
    dtype=np.float64
)
print(z)

#Numpy Addition
x = np.array([
    [1,2],
    [3,4]
])

y = np.array([
    [5,6],
    [7,8]
])

print('Numpy Addition: ', np.add(x,y))
print('Numpy Subtraction: ', np.subtract(x,y))
print('Numpy Multiplication: ', np.multiply(x,y))
print('Numpy Division: ', np.divide(x,y))