# -----------------------------------------------------------
# Experiment 1
# University Admission Analytics System
# -----------------------------------------------------------

import pandas as pd
import numpy as np


# -----------------------------------------------------------
# Function 1 : Load Dataset
# -----------------------------------------------------------
def load_dataset(file_name):
    try:
        df = pd.read_csv(file_name)
        print("\nDataset Loaded Successfully.")
        return df
    except Exception as e:
        print("Error Loading Dataset:", e)
        return None


# -----------------------------------------------------------
# Function 2 : Display Dataset Information
# -----------------------------------------------------------
def inspect_dataset(df):
    print("\n-------------------------------")
    print("FIRST 10 RECORDS")
    print("-------------------------------")
    print(df.head(10))

    print("\n-------------------------------")
    print("LAST 10 RECORDS")
    print("-------------------------------")
    print(df.tail(10))

    print("\nDataset Shape :", df.shape)

    print("\nColumn Names")
    print(df.columns.tolist())


# -----------------------------------------------------------
# Function 3 : Generate Profiling Report
# -----------------------------------------------------------
def profiling_report(df):
    print("\n===================================================")
    print("DATASET PROFILING REPORT")
    print("===================================================")

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Records :", df.duplicated().sum())

    print("\nMemory Usage")
    print(df.memory_usage(deep=True))

    print("\nUnique Values")
    for column in df.columns:
        print(f"{column} : {df[column].nunique()}")


# -----------------------------------------------------------
# Function 4 : Classify Attributes
# -----------------------------------------------------------
def classify_attributes(df):
    numerical = []
    categorical = []
    ordinal = []

    ordinal_columns = [
        "Admission_Status",
        "Reservation_Category",
        "Branch_Preference"
    ]

    for column in df.columns:
        if column in ordinal_columns:
            ordinal.append(column)
        elif pd.api.types.is_numeric_dtype(df[column]):
            numerical.append(column)
        else:
            categorical.append(column)

    print("\n===============================")
    print("ATTRIBUTE CLASSIFICATION")
    print("===============================")

    print("\nNumerical Features")
    print(numerical)

    print("\nCategorical Features")
    print(categorical)

    print("\nOrdinal Features")
    print(ordinal)


# -----------------------------------------------------------
# Function 5 : Identify Inconsistencies
# -----------------------------------------------------------
def check_inconsistencies(df):
    print("\n===================================")
    print("DATA QUALITY ANALYSIS")
    print("===================================")

    if "Application_No" in df.columns:
        duplicate_ids = df[df["Application_No"].duplicated()]
        print("\nDuplicate Application Numbers")

        if duplicate_ids.empty:
            print("No Duplicate Records")
        else:
            print(duplicate_ids)

    if "Entrance_Exam_Score" in df.columns:
        invalid_marks = df[
            (df["Entrance_Exam_Score"] < 0) |
            (df["Entrance_Exam_Score"] > 100)
        ]

        print("\nInvalid Entrance Exam Scores")
        print(invalid_marks)

    if "Board_Percentage" in df.columns:
        invalid_percentage = df[
            (df["Board_Percentage"] < 0) |
            (df["Board_Percentage"] > 100)
        ]

        print("\nInvalid Board Percentage")
        print(invalid_percentage)

    if "Age" in df.columns:
        invalid_age = df[
            (df["Age"] < 16) |
            (df["Age"] > 30)
        ]

        print("\nInvalid Age")
        print(invalid_age)


# -----------------------------------------------------------
# Function 6 : Admission Statistics Report
# -----------------------------------------------------------
def admission_statistics(df):
    print("\n===================================")
    print("ADMISSION STATISTICS REPORT")
    print("===================================")

    if "Branch_Preference" in df.columns:
        print("\nBranch Wise Applications")
        print(df["Branch_Preference"].value_counts())

    if "Reservation_Category" in df.columns:
        print("\nReservation Category")
        print(df["Reservation_Category"].value_counts())

    if "Admission_Status" in df.columns:
        print("\nAdmission Status")
        print(df["Admission_Status"].value_counts())

    if "Family_Income" in df.columns:
        print("\nAverage Family Income")
        print(df["Family_Income"].mean())

    if "Entrance_Exam_Score" in df.columns:
        print("\nHighest Entrance Score")
        print(df["Entrance_Exam_Score"].max())

        print("\nLowest Entrance Score")
        print(df["Entrance_Exam_Score"].min())


# -----------------------------------------------------------
# Function 7 : Clean Dataset
# -----------------------------------------------------------
def clean_dataset(df):
    df = df.drop_duplicates()

    if "Age" in df.columns:
        df = df[(df["Age"] >= 16) & (df["Age"] <= 30)]

    if "Entrance_Exam_Score" in df.columns:
        df = df[
            (df["Entrance_Exam_Score"] >= 0) &
            (df["Entrance_Exam_Score"] <= 100)
        ]

    if "Board_Percentage" in df.columns:
        df = df[
            (df["Board_Percentage"] >= 0) &
            (df["Board_Percentage"] <= 100)
        ]

    return df


# -----------------------------------------------------------
# Function 8 : Export Dataset
# -----------------------------------------------------------
def export_dataset(df):
    df.to_csv("UniversityAdmission_Cleaned.csv", index=False)
    print("\nCleaned Dataset Exported Successfully.")


# -----------------------------------------------------------
# Main Program
# -----------------------------------------------------------
def main():
    file_name = input("Enter Dataset Name : ")

    df = load_dataset(file_name)

    if df is not None:
        inspect_dataset(df)
        profiling_report(df)
        classify_attributes(df)
        check_inconsistencies(df)
        admission_statistics(df)

        clean_df = clean_dataset(df)
        export_dataset(clean_df)


if __name__ == "__main__":
    main()