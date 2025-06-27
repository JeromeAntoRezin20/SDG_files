import pandas as pd
import json
import os 
print("Current working Directory:", os.getcwd())
import random
from datetime import datetime, timedelta
 
# Load question templates
with open("question_templates.json", "r", encoding="utf-8") as f:
    question_templates = json.load(f)
 
# Predefined choices for various fields
designations = [
    "Software Engineer", "Senior Developer", "Tech Lead", "Manager", "Analyst",
    "QA Engineer", "Business Analyst", "Data Scientist", "System Architect", "DevOps Engineer",
    "Product Manager", "Intern", "Consultant", "UI/UX Designer", "Database Administrator"
]
projects = [
    "Orion", "Nova", "Helios", "Quantum", "Aether", "Phoenix", "Nimbus", "Atlas",
    "Horizon", "Zephyr", "Vortex", "Lumen", "Titan", "Cosmos", "Pioneer"
]
locations = [
    "Chennai", "Bangalore", "Hyderabad", "Pune", "Delhi", "Mumbai", "Kolkata",
    "Noida", "Gurgaon", "Ahmedabad", "Coimbatore", "Jaipur", "Trivandrum", "Nagpur", "Surat"
]
managers = [
    "Charlie Daniels", "Anita Roy", "Kiran Rao", "Preeti Nair", "Vikram Mehta",
    "Sneha Sharma", "Arun Iyer", "Deepa Reddy", "Raj Malhotra", "Divya Kapoor",
    "Siddharth Rao", "Priya Menon", "Karthik Shenoy", "Nidhi Joshi", "Rahul Mishra"
]
 
# Function to generate a random date between two years
def random_date(start_year=1980, end_year=2005):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime('%Y-%m-%d')
 
# Generate populated data from CSV
for part in range(1, 11):
    input_file = f"employee_dataset\employees_part_{part}.csv"
    output_file = f"employees_part_{part}.json"
 
    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        continue
 
    df = pd.read_csv(input_file)
 
    enriched_employees = []
 
    for _, row in df.iterrows():
        emp_id = str(row["Employee_ID"])
        emp_name = row["Employee_Name"]
        all_fields = {
            "Designation": random.choice(designations),
            "Project Name": random.choice(projects),
            "Reporting Manager": random.choice(managers),
            "Location": random.choice(locations),
            "DOJ": random_date(2010, 2022),
            "DOB": random_date(1980, 2000),
            "Email": f"{emp_id}@mail.com",
            "Phone": f"+91{random.randint(6000000000, 9999999999)}",
            "Laptop Serial No": f"LP-{random.randint(1000, 9999)}"
        }
 
        selected_fields = random.sample(list(all_fields.keys()), 6)
 
        # Assign values to selected fields; others stay blank
        final_fields = {}
        for field in all_fields:
            final_fields[field] = all_fields[field] if field in selected_fields else ""
 
        # Generate questions from selected fields
        questions = []
        for field in selected_fields:
            if field in question_templates:
                questions.append(random.choice(question_templates[field]))
 
        enriched_employees.append({
            "EmpID": emp_id,
            "EmpName": emp_name,
            "Fields": final_fields,
            "AuthenticationQuestions": questions
        })
 
    # Write to JSON file
    with open(output_file, "w", encoding="utf-8") as out:
        json.dump(enriched_employees, out, indent=4)
 
    print(f"✅ Generated: {output_file}")