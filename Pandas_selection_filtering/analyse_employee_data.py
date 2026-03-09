import pandas as pd

#converted the given data into csv file and stored in a folder
#given the folder path to convert into a pandas dataframe
employee_data=pd.read_csv("Pandas_selection_filtering\\pandas_employee.csv") #,index_col="EmployeeID")
#print(employee_data.head())


selected_columns=employee_data[["Name","Department","Salary"]]
#passsed a list of column names to get a dataframe of required columns 
print(selected_columns)

print(f"\nEmployee at row psition 5:\n{employee_data.iloc[5]}")

#display the employee with 208 using loc
#new_index=employee_data[employee_data,index_col="EmployeeID"]
#print(new_index)
#for this task we need to change the index for that i used set_index ,and used loc.
new_employee_data = employee_data.set_index('EmployeeID')
print("\n\n",new_employee_data.loc[208])


#all employees from the 'Engineering' department
engg_department=employee_data[employee_data["Department"]=="Engineering"]
print(f"\nengineering department Employees:\n{engg_department}")

#Filter and display all employees with Salary greater than 70000
print(f"\nEmployees with salary greater than 70000:\n{employee_data[employee_data["Salary"]>70000]}")

#Filter and display employees from 'Sales' department with Performance Score >= 4
print(f"\nEmployees with Performance Score >= 4:\n{employee_data[employee_data["Performance Score"]>=4]}")

#Sort the entire DataFrame by Salary in descending order and display the top 3 highest-paid employees
sorted_salary=employee_data.sort_values("Salary",ascending=False)
print(f"\n{sorted_salary.head(3)}")

#Sort by Department (ascending) and then by Salary (descending) within each department
sorted_employee_data=employee_data.sort_values(["Department","Salary"],ascending=[True,False])
print(sorted_employee_data)