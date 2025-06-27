from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import random
 
# Load employee data and model
df = pd.read_csv("enriched_employee_dataset_50000.csv")  # This should contain 'emp_id', 'dob', 'location', etc.
model = joblib.load("model.pkl")  # Your trained RandomForest model
 
# Initialize FastAPI app
app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# Request schema for validation
class AnswerInput(BaseModel):
    answers: list[str]
 
# Simulated question generator using employee fields
def generate_questions(emp_row):
    fields = ["dob", "location", "department", "project", "manager"]
    selected = random.sample(fields, 3)
    questions = [f"What is your {field.replace('_', ' ')}?" for field in selected]
    correct_values = [str(emp_row[field]) for field in selected]
    return questions, correct_values
 
# Endpoint to get questions
@app.get("/api/questions/{emp_id}")
def ask_questions(emp_id: str):
    emp_data = df[df["emp_id"] == emp_id]
    if emp_data.empty:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp_row = emp_data.iloc[0]
    questions, correct_answers = generate_questions(emp_row)
    # Store correct answers temporarily or return to client in a secure session in production
    return {"questions": questions, "correct_answers": correct_answers}  # Remove correct_answers in real apps
 
# Endpoint to validate answers
@app.post("/api/validate/{emp_id}")
def validate(emp_id: str, input_data: AnswerInput):
    emp_data = df[df["emp_id"] == emp_id]
    if emp_data.empty:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp_row = emp_data.iloc[0]
    _, correct_answers = generate_questions(emp_row)  # Should be securely stored and retrieved
    matches = sum([
        str(ans).strip().lower() == str(correct).strip().lower()
        for ans, correct in zip(input_data.answers, correct_answers)
    ])
    is_valid = matches >= 2
    return {"message": "Validation successful" if is_valid else "Validation failed"}