import pandas as pd

# load dataset
df = pd.read_csv("/home/friend/my_jupyter_project/MCA1/Aman sidar/PYTHON/PRACTICAL 1/student_performance.csv")

# first five records
print(df.head())

# shape of dataset
print("Shape:", df.shape)

# column names and data types
print("\nData Types:")
print(df.dtypes)

# missing values
print("\nMissing Values:")
print(df.isnull().sum())

# statistical summary
print("\nStatistical Summary:")
print(df.describe())
