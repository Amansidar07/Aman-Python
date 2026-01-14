import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(
    "/home/friend/my_jupyter_project/MCA1/Aman sidar/PYTHON/PRACTICAL 1/employee_data.csv"
)

# Histogram for Salary
plt.hist(df["Salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Box plot for Age
sns.boxplot(x=df["Age"])
plt.title("Age Box Plot")
plt.show()

# Bar chart for department-wise employee count
df["Department"].value_counts().plot(kind="bar")
plt.title("Employees per Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

# Scatter plot between Experience_Years and Salary
plt.scatter(df["Experience_Years"], df["Salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience Years")
plt.ylabel("Salary")
plt.show()

# Correlation heatmap
sns.heatmap(
    df[["Experience_Years", "Salary", "Age"]].corr(),
    annot=True
)
plt.title("Correlation Heatmap")
plt.show()
