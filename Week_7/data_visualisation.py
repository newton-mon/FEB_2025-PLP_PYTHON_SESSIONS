import matplotlib.pyplot as plt
import pandas as pd

# 2. Loading the Dataset
df = pd.read_csv('people-100.csv')

# Convert 'Date of birth' to datetime
df_cleaned['Date of birth'] = pd.to_datetime(df_cleaned['Date of birth'], errors='coerce')

# Create a new column for birth year
df_cleaned['Birth Year'] = df_cleaned['Date of birth'].dt.year

# Group by year and calculate average age
avg_age_by_year = df_cleaned.groupby('Birth Year')['Age'].mean()

# Plot line chart
plt.figure(figsize=(10, 5))
plt.plot(avg_age_by_year.index, avg_age_by_year.values, marker='o')
plt.title('Average Age by Year of Birth')
plt.xlabel('Birth Year')
plt.ylabel('Average Age')
plt.grid(True)
plt.tight_layout()
plt.show()



print("TASK 2")
# Group by Sex and compute average age
avg_age_by_sex = df_cleaned.groupby('Sex')['Age'].mean()

# Plot bar chart
plt.figure(figsize=(6, 4))
avg_age_by_sex.plot(kind='bar', color=['skyblue', 'lightgreen'])
plt.title('Average Age by Sex')
plt.xlabel('Sex')
plt.ylabel('Average Age')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()




print("TASK 3")
# Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(df_cleaned['Age'], bins=10, color='orange', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
