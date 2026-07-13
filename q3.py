import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

# Load dataset
file_path = "customer_data.csv"

df = pd.read_csv(file_path)

# ---------------------------------------
# Create Age Group
# ---------------------------------------

def age_group(age):
    if age < 18:
        return "Child"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

df["AgeGroup"] = df["Age"].apply(age_group)

# ---------------------------------------
# One-Hot Encoding
# ---------------------------------------

categorical_columns = df.select_dtypes(include=['object', 'string']).columns

encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')

encoded = encoder.fit_transform(df[categorical_columns])

encoded_df = pd.DataFrame(
    encoded,
    columns=encoder.get_feature_names_out(categorical_columns)
)

# Remove original categorical columns
df = df.drop(columns=categorical_columns)

# Merge encoded columns
df = pd.concat([df.reset_index(drop=True),
                encoded_df.reset_index(drop=True)], axis=1)

# ---------------------------------------
# Min-Max Scaling
# ---------------------------------------

numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

scaler = MinMaxScaler()

df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# ---------------------------------------
# Save CSV
# ---------------------------------------

output_file = "customer_data_transformed.csv"

df.to_csv(output_file, index=False)

print("Transformation Completed Successfully!")
print("Saved as:", output_file)