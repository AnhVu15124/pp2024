import tkinter as tk
from tkinter import messagebox
from domain import Student, Course, All_marks
import numpy as np

def list_students(students, all_marks, window):
    info = "Students' information\n"
    for student in students:
        info += f"_________________________________________\nID: {student.id}\nName: {student.name}\nDate of birth: {student.dob}\n"
        for all_mark in all_marks:
            if student.id in all_mark.marks:
                info += f"Mark for course {all_mark.course.id} is {all_mark.marks[student.id]}\n"
    messagebox.showinfo("Students' information", info)

def list_courses(courses, window):
    info = "Courses' information\n"
    for course in courses:
        info += f"_________________________________________\nID: {course.id}\nName: {course.name}\nCredit: {course.credit}\n"
    messagebox.showinfo("Courses' information", info)

def gpa(students, all_marks, courses):
    student_gpas = []
    for student in students:
        marks = np.array([all_mark.marks[student.id] for all_mark in all_marks if student.id in all_mark.marks], dtype=np.float64)
        course_ids = [all_mark.course.id for all_mark in all_marks if student.id in all_mark.marks]
        credits = np.array([course.credit for course in courses if course.id in course_ids], dtype=np.float64)
        total_point = np.sum(marks * credits)
        total_credits = np.sum(credits)
        gpa_value = total_point / total_credits
        student_gpas.append((student, gpa_value))
    sorted_students = sorted(student_gpas, key=lambda x: x[1], reverse=True)
    info = "Students list sorted by GPA:\n"
    for student, gpa_value in sorted_students:
        info += f"ID: {student.id}\nName: {student.name}\nDate of birth: {student.dob}\nGPA: {gpa_value:.1f}\n_________________________________________\n"
    messagebox.showinfo("Students list sorted by GPA", info)