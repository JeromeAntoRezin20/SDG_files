# Python Code
import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Function to generate random employee data
def generate_employee_data(num_records=1000):
    data = []
    locations = ['New York', 'San Francisco', 'Chicago', 'Los Angeles', 'Seattle', 'Austin']
    managers = ['John Doe', 'Jane Smith', 'Emily Davis', 'Michael Brown', 'Sarah Wilson']
    laptop_brands = ['Dell', 'HP', 'Lenovo', 'Apple', 'Asus']
    projects = ['Project Alpha', 'Project Beta', 'Project Gamma', 'Project Delta', 'Project Omega']
    designations = ['Software Engineer', 'Data Scientist', 'Product Manager', 'DevOps Engineer', 'UI/UX Designer']

    for _ in range(num_records):
        # Generate random employee details
        emp_id = fake.unique.random_int(min=1000, max=9999)
        name = fake.name()
        dob = fake.date_of_birth(minimum_age=22, maximum_age=60)
        doj = fake.date_between(start_date='-10y', end_date='today')
        location = random.choice(locations)
        reporting_manager = random.choice(managers)
        laptop_number = fake.unique.random_int(min=100000, max=999999)
        laptop_brand = random.choice(laptop_brands)
        project_involved = random.choice(projects)
        designation = random.choice(designations)

        # Randomly select 6 fields to fill for the employee
        all_fields = {
            'Employee ID': emp_id,
            'Employee Name': name,
            'Date of Birth': dob,
            'Date of Joining': doj,
            'Location': location,
            'Reporting Manager': reporting_manager,
            'Laptop Number': laptop_number,
            'Laptop Brand': laptop_brand,
            'Project Involved': project_involved,
            'Designation': designation
        }
        selected_fields = random.sample(list(all_fields.items()), 6)
        employee_data = {field: value for field, value in selected_fields}

        # Append to the dataset
        data.append(employee_data)

    return pd.DataFrame(data)

# Generate dataset
employee_data = generate_employee_data(num_records=1000)

# Save to CSV
employee_data.to_csv('random_employee_dataset.csv', index=False)

print("Employee dataset created and saved as 'random_employee_dataset.csv'.")



# Read the CSV file
file_path = 'employee_dataset.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())  # Displays the first 5 rows by default

# Optionally, display the entire dataset (not recommended for very large datasets)
# print(data)

# Display the shape of the dataset (rows, columns)
print("Dataset Shape:", data.shape)

# Display column names
print("Column Names:", data.columns.tolist())
