import pandas as pd

# Load CSV file
file_path = "customer_data.csv"

df = pd.read_csv(file_path)

# Display first 10 rows
print("\nFirst 10 Rows:")
print(df.head(10))

# Number of rows and columns
print("\nDataset Shape:")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())