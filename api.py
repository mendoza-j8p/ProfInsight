from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date

app = FastAPI()

# Simulación de datos
class Professor(BaseModel):
    date_of_entry: date
    name: str
    subject: str
    years_of_experience: int
    publications: int
    extra_courses: int
    current_salary: float

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Data Insight Pro API!",
        "endpoints": {
            "/profesores": "Get a list of professors",
            "/upload": "Upload a CSV file with professor data"
        },
        "documentation": "Refer to /docs for API documentation."
    }


@app.get("/professors", response_model=List[Professor])
def get_professors():
    # Implementa la lógica para obtener datos de la base de datos
    return [
        Professor(
            date_of_entry=date(2015, 9, 1),
            name="Dr. Ane Stone",
            subject="Mathematics",
            years_of_experience=10,
            publications=25,
            extra_courses=5,
            current_salary=3500.00
        )
    ]
