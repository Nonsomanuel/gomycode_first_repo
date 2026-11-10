import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
# pd.set_option('display.max_info_columns', None)


data = pd.read_csv("Popular_Baby_Names.csv")

df = data.rename(columns={
    "Child's First Name": 'First_Name',
    'Year of Birth': 'Year',
})

#Filtering for male entries from the year 2015
df_filtered = df.query('Year > 2015 and Gender == "MALE"')
# df_filtered.head()

# print(df_filtered)
# print(df_filtered.describe())
# print(df_filtered.info())

#Creating a new column with the assign function
# df_new = df.assign(Name_Length=df['First_Name'].str.len())
df_new = df.assign(Name_Length=df['First_Name'].apply(len))
# print(df_new)

#data sorting by name length
df_sorted = df_new.sort_values(by='Name_Length' , ascending=False)
# print(df_sorted)

#saving the sorted data to a new CSV file
# df_sorted.to_csv('sorted_baby_names.csv', index=False)

# print(df)
# print(data)
# print(data.info())
# print(data.describe(include='all'))

#Creatiing DataFrame with missing values
data = {
    "A": [1, 2, np.nan, 4, 5],
    "B": [np.nan, 2, 3, 4, 5],
    "C": [1, 2, 3, np.nan, 5],
    "D": [1, 2, 3, 4, 5]
}

# df = pd.DataFrame(data)

# print(df)

#Detecting outliers with z-score
# Create a DataFrame with sample data
df = pd.DataFrame({'Height': [170, 160, 130, 190, 180, 150, 140, 200, 175, 165]})

# Calculate the z-score of each data point
z_scores = np.abs(stats.zscore(df['Height']))
threshold = 3
outliers = df[z_scores > threshold]

# print("Outliers based on z-score:")
# print(outliers)

#Detecting outliers with IQR
Q1 = df["Height"].quantile(0.25)
Q3 = df["Height"].quantile(0.75)
# print(Q1)
# print(Q3)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Height"] < lower) |
    (df["Height"] > upper)
]
# print(outliers)
# print(IQR)


#Handling Duplicate Values
df = pd.DataFrame({
    "Name": ["John", "Anna", "John", "Mike"],
    "Age": [28, 22, 28, 20]
})

# print(df.duplicated())

df = df.drop_duplicates()
#
# print(df)

#Dictionary Mapping
df = pd.DataFrame({
    "Priority": [
        "Low", "Medium", "High",
        "Medium", "Low"
    ]
})
priority_mapping = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}
df["Priority_Encoded"] = (
    df["Priority"].map(priority_mapping)
)
# print(df)

#one-hot encoding
df = pd.DataFrame({
    "Fruit": [
        "Apple", "Orange", "Banana",
        "Banana", "Orange", "Apple"
   ]
})

one_hot_df = pd.get_dummies(
    df,
    columns=["Fruit"],
    dtype=int
)

# print(one_hot_df)


#Label  Encoding
fruits = [
"apple", "avocado", "banana", "banana",
"orange", "kiwi", "mango", "apple"
]
encoder = LabelEncoder()

encoded = encoder.fit_transform(fruits)

print(encoder.classes_)
print(encoded)





