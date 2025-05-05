import pandas as pd

# Load the dataset
try:
    df = pd.read_csv('owid-covid-latest.csv')
    print("Data loaded successfully!")
except FileNotFoundError:
    print("Error: The file 'owid-covid-latest.csv' was not found. Please ensure the file is in the correct directory.")
    exit()

# Check columns
print("\nColumns in the dataset:")
print(df.columns)

# Preview the first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Identify missing values
print("\nNumber of missing values per column:")
print(df.isnull().sum())


# 1. Filter countries of interest
countries_of_interest = ['United States', 'Canada']
df_filtered = df[df['location'].isin(countries_of_interest)].copy()
print("\nDataFrame filtered for United States and Canada:")



# Identify & Drop rows with missing critical values (e.g., total_cases)
print("\nNumber of missing values in 'total_cases' column before handling:", df_filtered['total_cases'].isnull().sum())
df_filtered.dropna(subset=['total_cases'], inplace=True)
print("Number of missing values in 'total_cases' column after dropping:", df_filtered['total_cases'].isnull().sum())



# 4. Handle missing numeric values
numeric_cols = df_filtered.select_dtypes(include=['number']).columns
print("\nNumeric columns in the filtered DataFrame:", numeric_cols)

# Fill missing numeric values using forward fill (ffill) followed by backward fill (bfill)
# This helps to propagate the last valid observation forward and the next valid observation backward.
df_filtered[numeric_cols] = df_filtered[numeric_cols].fillna(method='ffill').fillna(method='bfill')
print("\nNumber of missing values in numeric columns after filling:")
print(df_filtered[numeric_cols].isnull().sum())

print("\nCleaned and processed DataFrame (first 5 rows):")
print(df_filtered.head())




import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df_filtered (containing data for US and Canada with cleaned dates) is available

# 1. Plot total cases over time for selected countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='total_cases', hue='location')
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend(title='Country')
plt.grid(True)
plt.show()

# 2. Plot total deaths over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='total_deaths', hue='location')
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend(title='Country')
plt.grid(True)
plt.show()

# 3. Compare trends in new cases over time (weekly) between countries
df_weekly_cases = df_filtered.groupby(['location', pd.Grouper(key='date', freq='W')])['new_cases'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_weekly_cases, x='date', y='new_cases', hue='location')
plt.title('Weekly New COVID-19 Cases Over Time')
plt.xlabel('Week Ending Date')
plt.ylabel('Total New Cases (Weekly)')
plt.legend(title='Country')
plt.grid(True)
plt.show()

# 4. Calculate the death rate: total_deaths / total_cases
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='death_rate', hue='location')
plt.title('COVID-19 Death Rate Over Time (Total Deaths / Total Cases)')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend(title='Country')
plt.grid(True)
plt.show()

print("\nFirst few rows with calculated death rate:")
print(df_filtered.head())


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  # For Choropleth maps

# Assuming df (original, unfiltered dataframe) and df_filtered are available
# and that df_filtered contains 'location' and 'date'

# --- 6. Visualizing Vaccination Progress ---

# 6.1 Plot cumulative vaccinations over time for selected countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='total_vaccinations', hue='location')
plt.title('Cumulative COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend(title='Country')
plt.grid(True)
plt.show()

# 6.2 Compare % vaccinated population over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y='people_vaccinated_per_hundred', hue='location')
plt.title('Percentage of Population Vaccinated Over Time')
plt.xlabel('Date')
plt.ylabel('Percentage of Population Vaccinated')
plt.legend(title='Country')
plt.grid(True)
plt.show()

# --- 7. Optional: Build a Choropleth Map ---
# Prepare data for the latest date for choropleth
latest_date_df = df[df['date'] == df['date'].max()].copy() # Make a copy to avoid modifying the original
latest_date_df = latest_date_df[['iso_code', 'total_cases', 'location']] # Select only relevant columns. location is needed for the title.
latest_date_df.dropna(subset=['iso_code', 'total_cases'], inplace=True) # Drop rows where iso_code or total_cases is missing.  Important for the map.

# Choropleth Map of Total Cases on the Latest Date
if not latest_date_df.empty: # Check if the dataframe is empty
    fig = px.choropleth(latest_date_df,
                        locations="iso_code",
                        color="total_cases",
                        hover_name="location", # Add hover name
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title=f"Total COVID-19 Cases on {df['date'].max()}", # Use f-string
                        projection='natural earth')  # Set the projection
    fig.show()
else:
    print("Skipping Choropleth map: No data available for the latest date.")

# --- 8. Insights & Reporting ---

#  Example Insights (These need to be replaced with actual insights
#  from the data analysis)
insights = [
    "Both the United States and Canada experienced a surge in total cases in late 2021, likely due to the Delta variant.",
    "Canada has a higher percentage of its population vaccinated compared to the United States.",
    "The death rate (total deaths / total cases) has generally declined over time in both countries, possibly due to vaccinations and improved treatment.",
    "Weekly new cases show a recurring seasonal pattern, with peaks in the winter months.",
    "The choropleth map shows that the total cases are unevenly distributed across the world."
]
print("\nInsights:")
for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}")

print("\nDeliverables:")
print("A well-documented Jupyter Notebook combining:")
print(" - Code")
print(" - Visualizations")
print(" - Narrative explanations")
print("Optional export: Notebook -> PDF or a PowerPoint with screenshots")
