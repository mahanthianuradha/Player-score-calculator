import pandas as pd
import numpy as np

#Task 1: Load and Inspect the Data

data = {
    'transaction_id': range(1, 21),
    'date': pd.date_range('2024-10-01', periods=20, freq='D'),
    'region': ['North', 'South', 'East', 'West', None, 'North', 'South', None, 'East', 'West',
               'North', 'South', 'East', 'West', 'North', None, 'East', 'West', 'North', 'South'],
    'product_category': ['Electronics', 'Clothing', None, 'Books', 'Electronics', 'Home', 
                         'Clothing', 'Books', 'Electronics', None, 'Home', 'Clothing', 
                         'Books', 'Electronics', 'Home', 'Clothing', 'Books', 'Electronics', 
                         'Home', 'Clothing'],
    'sales_amount': [1200, 450, 890, None, 1500, 670, None, 340, 2100, 780, 
                     560, None, 420, 1800, 920, 510, 380, None, 1100, 640],
    'quantity': [2, 5, 3, 1, None, 4, 2, 3, 1, 5, 
                 3, 2, None, 1, 4, 3, 2, 1, None, 4],
    'customer_age': [25, 34, None, 45, 29, None, 38, 52, 27, 41, 
                     33, None, 48, 26, 35, 42, None, 31, 39, 44],
    'payment_method': ['Credit Card', 'UPI', 'Cash', 'Debit Card', 'Credit Card', 
                       'UPI', 'Cash', None, 'Credit Card', 'UPI', 'Debit Card', 
                       'Cash', 'Credit Card', None, 'UPI', 'Cash', 'Debit Card', 
                       'Credit Card', 'UPI', None]
}

df = pd.DataFrame(data)
print(df)
print(f"\n\n\nDisplay basic information:\n{df.info()}")
print(f"\n\n\nCount missing values in each column:\n{df.isna().sum()}")

#Task 2: Handle Missing Values
#1.Region & Product_category: Fill with mode (most frequent value)
columns_to_fill=["region","product_category"]
df[columns_to_fill]= df[columns_to_fill].fillna(df[columns_to_fill].mode().iloc[0])
print("\n\n New Region & Product_category : ")
print(df)
#mode_values=df["Region"].mode()[0]
#print(mode_values)

#2.Sales_amount: Fill with median

#df=df.fillna(df['sales_amount'].median()[0])
sales_amount_median = df['sales_amount'].median()
df["sales_amount"] = df['sales_amount'].fillna(sales_amount_median)
#print("\n\n\nSales_amount filled with median: ")
#print(df)

#3.Quantity: Fill using forward fill (ffill)

df['quantity'] = df['quantity'].ffill()
#print("\n\n\nQuantity after using forward fill:")
#print(df)

#4.Customer_age: Fill with mean (rounded to integer)
customer_age_mean = df['customer_age'].mean().round(0).astype(int)
df['customer_age'] =  df['customer_age'].fillna(customer_age_mean)
#print("\n\n\nCustomer_age after Filled with mean:")
#print(df)

#5.Payment_method: Drop rows where payment_method is missing
df=df.dropna(subset=['payment_method'])
#print("\n\n\nDropped rows where payment_method is missing:")
print("\n\nCleaned Data:")
print(df)
print(f"\n\n\nCount missing values in each column:\n{df.isna().sum()}")

#Task 3: GroupBy Analysis
#1.Calculate total sales by region
total_sales_byregion=df.groupby('region')['sales_amount'].sum()
print("\n\n\nTotal sales by region:")
print(total_sales_byregion)

#2.Calculate average sales by product_category
average_sales=df.groupby('product_category')['sales_amount'].mean()
print("\n\n\nAverage sales by product_category:")
print(average_sales)

#3.Group by both region and product_category, calculate total sales and quantity, then use reset_index() to flatten
flatten_index=df.groupby(['region','product_category']).agg({'sales_amount':[sum],
                                                           'quantity':[sum]}).reset_index()
print(flatten_index) 

#4.Display top 3 region-product combinations by sales
top3_sales_regions = df.groupby(['region','product_category'])['sales_amount'].sum().sort_values(ascending=False).head(3)
print("\n\n\ntop 3 region-product combinations by sales:")
print(top3_sales_regions)
                                                        
#Task 4: Custom Aggregation
#1.Create a function sales_range() that returns max - min of sales
def sales_range (x):
    return x.max() - x.min()

#2.Apply it to find sales range for each region
range_of_sales=df.groupby('region')['sales_amount'].agg(['max','min',sales_range])
print("\n\n\n Max - Min and sales range for each region:")
print(range_of_sales)

#3.Use .agg() to calculate multiple metrics by region
   #sales_amount: sum, mean, max
   #quantity: sum, min
multiple_metrics_by_region=df.groupby('region').agg({'sales_amount': ['sum', 'mean' , 'max'],
                                                      'quantity': ['sum', 'min']})
print("\n\n\n Multiple metrics by region:")
print(multiple_metrics_by_region)