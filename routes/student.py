from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentsEntity

student_router = APIRouter()

@student_router.get('/hello')
async def hello_world():
    return {"message": "Hello World"}
    
    
@student_router.get('/students')
async def find_all_students():    
    return listOfStudentsEntity(connection.local.student.find())

@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentsEntity(connection.local.student.find())

