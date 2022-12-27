from pydantic import BaseModel
from typing import Optional
class post_student_data(BaseModel):
     name:str
     age :int
     roll_no:str

class put_student_data(BaseModel):
    name:Optional[str]
    age:Optional[int]
    roll_no:Optional[str]