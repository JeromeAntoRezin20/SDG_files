import json
import random
import os
from datetime import datetime, timedelta
 
# Define all possible files
file_list = [f"employees_part_{i}.json" for i in range(1, 11)]
 
# ✅ Option 1: Randomly pick 3 files
# selected_files = random.sample(file_list, 3)
 
# ✅ Option 2: Hardcode specific file names
selected_files = [
    "populated_dataset\employees_part_4.json",
    "populated_dataset\employees_part_5.json",
    "populated_dataset\employees_part_6.json"
]
 
# Load question templates
with open("question_templates.json", "r", encoding="utf-8") as f:
    question_templates = json.load(f)
 
# Field value pools
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
 
# Date generators
def random_date(start_year=1980, end_year=2005):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime('%Y-%m-%d')
 
# Field-wise value generator
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
 
# Fields allowed for update
updatable_fields = [
    "Designation", "Project Name", "Reporting Manager", "Location", "Laptop Serial No"
]
 
# Fields to be preserved
locked_fields = ["DOJ", "DOB", "Email", "Phone"]
 
# Process each selected file
for file_name in selected_files:
    if not os.path.exists(file_name):
        print(f"❌ File not found: {file_name}")
        continue
 
    print(f"🔄 Enriching {file_name}...")
 
    with open(file_name, "r", encoding="utf-8") as f:
        employees = json.load(f)
 
    enriched_employees = []
 
    for emp in employees:
        emp_id = emp.get("EmpID", "")
        emp_name = emp.get("EmpName", "")
        current_fields = emp.get("Fields", {})
 
        # Select up to 6 fields to update (excluding locked fields)
        selected_to_update = random.sample(updatable_fields, min(6, len(updatable_fields)))
 
        updated_fields = current_fields.copy()
        change_log = {}
 
        for field in selected_to_update:
            old_value = current_fields.get(field, "")
            new_value = generate_random_value(field, emp_id)
            updated_fields[field] = new_value
            change_log[field] = {
                "old": old_value if old_value else " ",
                "new": new_value
            }
 
        # Restore the original values of locked fields
        for field in locked_fields:
            updated_fields[field] = current_fields.get(field, "")
 
        # Generate authentication questions from updated fields
        auth_questions = []
        for field in selected_to_update:
            if updated_fields.get(field) and field in question_templates:
                auth_questions.append(random.choice(question_templates[field]))
 
        enriched_employees.append({
            "EmpID": emp_id,
            "EmpName": emp_name,
            "Fields": updated_fields,
            "AuthenticationQuestions": auth_questions,
            "ChangeLog": change_log
        })
 
    # Save enriched data
    enriched_file = file_name.replace(".json", "_enriched.json")
    with open(enriched_file, "w", encoding="utf-8") as f:
        json.dump(enriched_employees, f, indent=4)
 
    print(f"✅ Saved enriched file: {enriched_file}")