from faker import Faker
import pandas as pd
import random

# Initialize Faker
fake = Faker('en_IN')  # Indian locale

# Number of students
num_students = 50

students = []

for i in range(1, num_students + 1):
    student = {
        "Student_ID": f"STU{i:04d}",
        "First_Name": fake.first_name(),
        "Last_Name": fake.last_name(),
        "Gender": random.choice(["Male", "Female"]),
        "Age": random.randint(18, 25),
        "Date_of_Birth": fake.date_of_birth(minimum_age=18, maximum_age=25),
        "Email": fake.email(),
        "Phone_Number": fake.phone_number(),
        "Address": fake.address().replace("\n", ", "),
        "City": fake.city(),
        "State": fake.state(),
        "PIN_Code": fake.postcode(),
        "Department": random.choice([
            "Computer Science",
            "Information Science",
            "Electronics",
            "Mechanical",
            "Civil",
            "Electrical",
            "Artificial Intelligence",
            "Data Science"
        ]),
        "Year": random.choice([1, 2, 3, 4]),
        "Semester": random.choice([1, 2, 3, 4, 5, 6, 7, 8]),
        "Section": random.choice(["A", "B", "C"]),
        "CGPA": round(random.uniform(5.5, 10.0), 2),
        "Attendance (%)": round(random.uniform(60, 100), 2),
        "Blood_Group": random.choice([
            "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"
        ]),
        "Guardian_Name": fake.name(),
        "Guardian_Phone": fake.phone_number()
    }

    students.append(student)

# Create DataFrame
df = pd.DataFrame(students)

# Save to Excel
file_name = "Fake_Student_Data.xlsx"
df.to_excel(file_name, index=False)

print(f"Excel file '{file_name}' created successfully!")