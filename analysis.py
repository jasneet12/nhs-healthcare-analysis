import pandas as pd

#load the data
df = pd.read_csv('hosp-epis-stat-admi-other-2022-23-data.csv')
# Show first 5 rows
print(df.head())

# Show column names
print("\nColumns:")
print(df.columns)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())