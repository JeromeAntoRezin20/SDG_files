import csv
from faker import Faker
import os
 
fake = Faker()
total_employees = 1_000_000
employees_per_file = 100_000
output_folder = "employee_dataset"
 
# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)
 
# Generate 1 million unique employee records
used_ids = set()
base_id = 20000000  # Starts with '2000'
 
def generate_unique_id():
    global base_id
    base_id += 1
    return str(base_id)
 
print("Generating and writing data...")
 
for file_num in range(1, (total_employees // employees_per_file) + 1):
    filename = os.path.join(output_folder, f"employees_part_{file_num}.csv")
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Employee_ID", "Employee_Name"])  # Header
 
        for _ in range(employees_per_file):
            emp_id = generate_unique_id()
            emp_name = fake.name()
            writer.writerow([emp_id, emp_name])
    
    print(f"File {file_num} written: {filename}")
 
print("Dataset generation complete.")