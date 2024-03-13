import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

class All_marks:
    def __init__(self):
        self.course = None
        self.marks = {}