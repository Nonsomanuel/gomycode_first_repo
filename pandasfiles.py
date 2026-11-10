import  numpy as np
import pandas as pd

# numbers = np.array([10, 20, 30])
# scores = pd.Series(numbers)
# print(numbers)
# print(scores)
#
#
# #Setting my index manually
# students = pd.Series(
# [75, 82, 91],
# index=["Ada", "John", "Mary"]
# )
#
# print(students)
#
# #Creating series from a list
# product = ["A", "B", "C", "D"]
# product_series = pd.Series(product)
# print(type(product))
# print(type(product_series))

# Defining the colors and their occurrences
colors = ["pink", "white", "black", "blue"]
occurrences = [20, 15, 6, 43]
# Creating the Series with a custom index
color_series = pd.Series(occurrences, index=colors)
# print(color_series)

#Series addition
# Define the colors and their corresponding values in two different series
colors = ["pink", "white", "black", "blue"]
S1 = pd.Series([20, 15, 6, 43], index=colors)
S2 = pd.Series([3, 22, 9, 10], index=colors)
# Adding the two series
result = S1 + S2
# print(result)

#Pandas DataFrame
data = {
    "Name": ["Ada", "John", "Mary"],
    "Age": [22, 25, 21],
    "Score": [85.5, 78.0, 92.0]}
df = pd.DataFrame(data)
# print(df)

#Creating custom index
# Define data using a dictionary with lists
data = {
    "ProductName": ["Product 1", "Product 2", "Product 3"],
    "ProductPrice": [10, 20, 30]}
# Create the DataFrame with a custom index
df = pd.DataFrame(data, index=['A', 'B', 'C'])
# print(df)

#Access Element using the index
# print(df.loc["B"])

#Data Alignment
names = pd.Series(["Ada", "John"], index=[0, 1])
scores = pd.Series([90, 75], index=[1, 0])
df = pd.DataFrame({    "Name": names,    "Score": scores})
# print(df)

#Data selection in Pandas
data = {
    "Name": ["John", "Jack", "Angelica", "Andrew"],
    "Age": [23, 20, 21, 22],
    "Home Address": [
         "Los Angeles",
         "California",
         "New York",
         "Florida"
    ]
}
df = pd.DataFrame(data)
new_data = df[['Age', 'Home Address']]
# print(df)
# print(new_data)

#loc selection
df = pd.DataFrame({
     "Age": [23, 20, 21, 22],
     "Role": ["AI", "AI", "WEB1", "WEB2"]
})
df.index = ["Jack", "Thomas", "Alexandre", "Anne"]
selected_data = df.loc[["Jack", "Thomas"]]
# print(selected_data)

#iloc selection
df = pd.DataFrame({
     "Name": ["John", "Jack", "Angelica", "Andrew"],
     "Last Name": ["Stott", "Mcbride", "Newman", "Hines"],
     "Age": [23, 20, 21, 22],    "Role": ["AI", "AI", "WEB1", "WEB2"],
"Home Address": [
        "Los Angeles",
        "California",
        "New York",
        "Florida"
    ]
})
selected_columns = df.iloc[:, 1:3]
print(df)
print(selected_columns)


