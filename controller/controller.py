from app import app
from data.dataconfig import students
from typing import Optional
from model.model_class import *

@app.get("/student")
def get_student_details(name:Optional[str]=None):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
        return {"message":"Data is not found"}

@app.get("/student/{user_id}")
def get_user(user_id:int):
    return students[user_id]

@app.post("/student/{student_id}")
def post_data(student_id:int,student_data:post_student_data):
    if student_id in students:
        return {"message":"User already Exists"}

    students[student_id] = student_data
    return students[student_id]
    
@app.put("/student/{student_id}")
def put_data(student_id:int,student_update:put_student_data):
    if student_id not in students:
        return {"message":"User not exits"}
    if student_update.name !=None:
        students[student_id] = student_update.name
    if student_update.age!=None:
        students[student_id] = student_update.age
    if student_update.roll_no !=None:
        students[student_id] = student_update.roll_no
    students[student_id] = student_update
    return students[student_id]
