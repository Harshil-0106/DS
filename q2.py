import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "customer_data.csv"

df = pd.read_csv(file_path)

# Select numerical columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

# ----------------------------
# Histogram
# ----------------------------
import math

rows = math.ceil(len(numerical_columns) / 2)

plt.figure(figsize=(12, rows * 4))

for i, column in enumerate(numerical_columns, 1):
    plt.subplot(rows, 2, i)
    sns.histplot(df[column], kde=True)
    plt.title(column)

plt.tight_layout()
plt.show()

# ----------------------------
# Box Plot
# ----------------------------
rows = math.ceil(len(numerical_columns) / 2)

plt.figure(figsize=(12, rows * 4))

for i, column in enumerate(numerical_columns, 1):
    plt.subplot(rows, 2, i)
    sns.boxplot(x=df[column])
    plt.title(column)

plt.tight_layout()
plt.show()