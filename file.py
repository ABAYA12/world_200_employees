import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read the csv file
file = pd.read_csv('employees.csv')
# convert the file to a dataframe
file_df = pd.DataFrame(file)
# replace null values with N/A
file_df.fillna('N/A')
# find the average salary
file_df['average salary'] = file_df['salary(usd)'].mean()


# 1 What is the average salary of employees in each department?
file_df['avg_dept_salary'] = file_df.groupby(
    'department')['salary(usd)'].transform('mean')

# 2 department salary percent
file_df['dept_salary_percentage'] = ((file_df.groupby('department')[
                                     'salary(usd)'].transform('sum') / file_df['salary(usd)'].sum()) * 100).round(2)

# save changes to employees.csv
file_df.to_csv('employees.csv', index=False)

# convert avg_dept_salary to an array
avg_dept_salary = np.array(file_df['avg_dept_salary'])

# plot a bar graph
plt.bar(file_df['department'], avg_dept_salary)
plt.title('World Departments Average Salary Distribution')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()

print('Loading...........................................Done!')
print(len(file_df))
