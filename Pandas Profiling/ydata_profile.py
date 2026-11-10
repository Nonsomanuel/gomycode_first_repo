import os
import webbrowser

import pandas as pd
from ydata_profiling import ProfileReport

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#Readiing the dataset
Popular_baby_names_df = pd.read_csv("Popular_Baby_Names.csv")

df = pd.DataFrame(Popular_baby_names_df)

# print(f'First 5 Rows: \n {df.head()}')
# print(f'Last 5 Rows: \n {df.tail()}')
# print(df.columns)
# print(df.shape)
# df.info()
# print(df.describe())

#Generating a Profile Report
profile = ProfileReport(df, title="Popular Baby Names Profiling Report", explorative=True)

#To display the report in a Jupyter Notebook.
# profile.to_notebook_iframe()

# Export to HTML
output_file = "popular_baby_names_report.html"
profile.to_file(output_file)

# Open the report in your default browser
webbrowser.open("file://" + os.path.abspath(output_file))

