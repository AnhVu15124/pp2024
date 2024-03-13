import tkinter as tk
from tkinter import messagebox
from domain import Student, Course, All_marks
import math

def input_students(window):
    num_students = tk.simpledialog.askinteger("Number of students", "Enter the number of students in this class:")
    if num_students is not None and num_students > 0:
        messagebox.showinfo("Success", "Number of students has been entered successfully.")
        return num_students
    else:
        messagebox.showerror("Error", "The number of students must be a positive number.")
        return 0
    
def input_courses(window):
    num_courses = tk.simpledialog.askinteger("Number of courses", "Enter the number of courses in this class:")
    if num_courses is not None and num_courses > 0:
        messagebox.showinfo("Success", "Number of courses has been entered successfully.")
        return num_courses
    else:
        messagebox.showerror("Error", "The number of courses must be a positive number.")
        return 0
    
def input_students_info(window, num_students):
    students = []
    with open("students.txt","w") as file:
        for i in range(num_students):
            id = tk.simpledialog.askstring(f"Student {i+1} ID",f"Enter student {i+1} id:")
            name = tk.simpledialog.askstring(f"Student {i+1} name",f"Enter student {i+1} name:")
            dob = tk.simpledialog.askstring(f"Student {i+1} date of birth",f"Enter student {i+1} date of birth (dd/mm/yyyy):")
            student = Student(id, name, dob)
            students.append(student)
            file.write(f"ID: {student.id}\nName: {student.name}\nDate of birth: {student.dob}\n_________________________________________________________________\n")
    messagebox.showinfo("Success", "Students' information has been entered successfully.")
    return students

def input_courses_info(window, num_courses):
    courses = []
    with open("courses.txt","w") as file:
        for i in range(num_courses):
            id = tk.simpledialog.askstring(f"Course {i+1} ID",f"Enter course {i+1} id:")
            name = tk.simpledialog.askstring(f"Course {i+1} name",f"Enter course {i+1} name:")
            credit = tk.simpledialog.askstring(f"Course {i+1} credit",f"Enter course {i+1} credit:")
            course = Course(id, name, credit)
            courses.append(course)
            file.write(f"ID: {course.id}\nName: {course.name}\nDate of birth: {course.credit}\n_________________________________________________________________\n")
    messagebox.showinfo("Success", "Courses' information has been entered successfully.")
    return courses

def input_marks(students, course, window):
    all_mark = All_marks()
    all_mark.course = course

    for student in students:
        mark = tk.simpledialog.askfloat(f"Mark for student {student.id}",f"Enter mark for student {student.name} - {student.id}:")
        mark = math.floor(mark * 10) /10
        all_mark.marks[student.id] = mark
    
    with open("marks.txt","a") as file:
        for student in students:
            if student.id in all_mark.marks:
                file.write(f"Student ID: {student.id}\nCourse ID: {course.id}\nMark: {all_mark.marks[student.id]}\n_________________________________________________________________\n")
    messagebox.showinfo("Success", "Marks have been entered successfully.")
    return all_mark