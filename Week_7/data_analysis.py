# 1. Importing Necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt

# 2. Loading the Dataset
df = pd.read_csv('people-100.csv')

# Preview the first few rows
print("Preview of the dataset:")
print(df.head())

# 4. Explore the structure of the dataset
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())



print("TASK 2")
print ("Task 2.1")

# 1. Compute basic statistics of numerical columns (Age)
print("Basic statistics for Age column:")
print(df_cleaned['Age'].describe())

# 2. Group by 'Sex' and compute average Age
print("\nAverage age by sex:")
print(df_cleaned.groupby('Sex')['Age'].mean())

# 3. Group by 'Job Title' and compute average Age (optional, might be many job titles)
print("\nAverage age by job title (top 10 shown):")
print(df_cleaned.groupby('Job Title')['Age'].mean().sort_values(ascending=False).head(10))


print("TASK 3")
