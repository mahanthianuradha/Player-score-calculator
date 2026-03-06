

import pandas as pd

#Task 1:
#url = "https://drive.google.com/file/d/1Mlu9r3afSGz5_02Y3wDJoQLpXszQXaIU/view?usp=sharing"

url = "https://drive.google.com/uc?id=1Mlu9r3afSGz5_02Y3wDJoQLpXszQXaIU"


df = pd.read_csv(url,index_col="order_id")
#should give index col to make order id as the index
print(df.head())
print(df.tail())

print("\n****Task2****\n")
#Task :2
#Structural inspection:
print(df.info()) 
print("\nShape:", df.shape)
print("\ncolumn names:",df.columns)
print("\nData types:\n", df.dtypes)
print("\nMissing values per column:\n", df.isnull().sum())
#Number of rows:20, Number of columns:6
#Quantity and order date columns  have 4 missing values each
# order_date column needs a data type conversion before any date-based analysis, using pd.to_datetime() function.

print("\n****TAsk:3****\n")
#Task : 3
print(df.describe())
print(df["unit_price"].median())
#Yes, unit_price appear to be skewed.By observing the output values it appears that 75% of the data is below mean
#  hence the data is not symmetrical but skewed.  





