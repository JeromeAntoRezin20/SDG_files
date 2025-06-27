import json
import random
import os
from datetime import datetime, timedelta
 
# ---- 1. Define input files ----
selected_files = [
    "populated_dataset\employees_part_1.json",
    "populated_dataset\employees_part_2.json",
    "populated_dataset\employees_part_3.json"
]
 
# ---- 2. Load question template ----
with open("question_templates.json", "r", encoding="utf-8") as f:
    question_templates = json.load(f)
 
# ---- 3. Field options ----
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
 
# ---- 4. Helpers ----
def random_date(start_year=1980, end_year=2005):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime('%Y-%m-%d')
 
def generate_random_value(field, emp_id):
    if field == "Designation":
        return random.choice(designations)
    elif field == "Project Name":
        return random.choice(projects)
    elif field == "Reporting Manager":
        return random.choice(managers)
    elif field == "Location":
        return random.choice(locations)
    elif field == "DOJ":
        return random_date(2010, 2022)
    elif field == "DOB":
        return random_date(1980, 2000)
    elif field == "Email":
        return f"{emp_id}@mail.com"
    elif field == "Phone":
        return f"+91{random.randint(6000000000, 9999999999)}"
    elif field == "Laptop Serial No":
        return f"LP-{random.randint(1000, 9999)}"
    return ""
 
# ---- 5. Field list ----
all_fields = [
    "Designation", "Project Name", "Reporting Manager", "Location",
    "DOJ", "DOB", "Email", "Phone", "Laptop Serial No"
]
 
# ---- 6. Start cloning ----
emp_id_counter = 30000000
 
for file_name in selected_files:
    if not os.path.exists(file_name):
        print(f"❌ File not found: {file_name}")
        continue
 
    with open(file_name, "r", encoding="utf-8") as f:
        employees = json.load(f)
 
    cloned_employees = []
 
    for emp in employees:
        emp_name = emp.get("EmpName", "")
        new_emp_id = str(emp_id_counter)
        emp_id_counter += 1
 
        # Pick 6 random fields to populate
        selected_fields = random.sample(all_fields, 6)
 
        new_fields = {}
        for field in all_fields:
            if field in selected_fields:
                new_fields[field] = generate_random_value(field, new_emp_id)
            else:
                new_fields[field] = ""
 
        # Generate 1 question per populated field
        auth_questions = []
        for field in selected_fields:
            if field in question_templates:
                auth_questions.append(random.choice(question_templates[field]))
 
        cloned_employees.append({
            "EmpID": new_emp_id,
            "EmpName": emp_name,
            "Fields": new_fields,
            "AuthenticationQuestions": auth_questions
        })
 
    # ---- 7. Save per file ----
    output_file = file_name.replace(".json", "_cloned.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(cloned_employees, f, indent=4)
 
    print(f"✅ Saved cloned data to: {output_file}")