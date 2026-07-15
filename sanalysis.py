import pandas as pd
import matplotlib.pyplot as plt

# ===========================
# Load Data
# ===========================
df = pd.read_excel("Fake_Student_Data.xlsx")

print("=" * 50)
print("STUDENT DATA ANALYSIS")
print("=" * 50)

# ===========================
# Basic Information
# ===========================
print("\nTotal Students :", len(df))
print("Departments    :", df["Department"].nunique())
print("Average CGPA   :", round(df["CGPA"].mean(), 2))
print("Average Attendance :", round(df["Attendance (%)"].mean(), 2), "%")

# ===========================
# Overall Topper
# ===========================
print("\nOVERALL TOPPER")
topper = df.loc[df["CGPA"].idxmax()]

print(topper[
    ["Student_ID",
     "First_Name",
     "Last_Name",
     "Department",
     "CGPA",
     "Attendance (%)"]
])

# ===========================
# Department-wise Toppers
# ===========================
print("\nDEPARTMENT-WISE TOPPERS")

dept_top = df.loc[df.groupby("Department")["CGPA"].idxmax()]

print(dept_top[
    ["Department",
     "First_Name",
     "Last_Name",
     "CGPA"]
])

# ===========================
# Average CGPA by Department
# ===========================
print("\nAVERAGE CGPA BY DEPARTMENT")

avg = df.groupby("Department")["CGPA"].mean()

print(avg)

# ===========================
# Student Count
# ===========================
print("\nSTUDENTS IN EACH DEPARTMENT")

print(df["Department"].value_counts())

# ===========================
# Dashboard
# ===========================

fig, ax = plt.subplots(2, 2, figsize=(14, 10))
plt.subplots_adjust(hspace=0.5, wspace=0.4)

# ---------------------------
# 1 Average CGPA
# ---------------------------
avg.plot(
    kind="bar",
    ax=ax[0,0]
)

ax[0,0].set_title("Average CGPA by Department")
ax[0,0].set_ylabel("CGPA")
ax[0,0].tick_params(axis='x', rotation=30)

# ---------------------------
# 2 Student Count
# ---------------------------
df["Department"].value_counts().plot(
    kind="bar",
    ax=ax[0,1]
)

ax[0,1].set_title("Students by Department")
ax[0,1].set_ylabel("Students")
ax[0,1].tick_params(axis='x', rotation=30)

# ---------------------------
# 3 Gender Distribution
# ---------------------------
df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax[1,0]
)

ax[1,0].set_ylabel("")
ax[1,0].set_title("Gender Distribution")

# ---------------------------
# 4 Attendance vs CGPA
# ---------------------------
ax[1,1].scatter(
    df["Attendance (%)"],
    df["CGPA"]
)

ax[1,1].set_title("Attendance vs CGPA")
ax[1,1].set_xlabel("Attendance (%)")
ax[1,1].set_ylabel("CGPA")
ax[1,1].grid(True)

plt.suptitle("Student Data Analysis Dashboard", fontsize=16)

plt.tight_layout()

plt.show()

print("\nAnalysis Completed Successfully!")