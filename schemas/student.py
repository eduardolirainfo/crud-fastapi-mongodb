
def studentEntity(db_item) -> dict:
    return{
        "id": str(db_item["_id"]),
        "student_name": db_item["student_name"],
        "student_email": db_item["student_email"],
        "student_phone": db_item["student_phone"]
    }
    
    
def listOfStudentsEntity(db_items) -> list:
    list_of_students = []
    
    for item in db_items:
        list_of_students.append(studentEntity(item))
            
    return list_of_students