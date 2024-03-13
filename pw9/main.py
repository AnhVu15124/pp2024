import tkinter as tk
from tkinter import simpledialog, messagebox
import zlib
import pickle
import threading
from input import *
from output import * 
from domain import Student, Course, All_marks

def compress_data(students, courses, all_marks):
    def compress():
        data = (students, courses, all_marks)
        compress_data = zlib.compress(pickle.dumps(data))
        with open("students.dat","wb") as file:
            file.write(compress_data)
    threading.Thread(target=compress).start()

def decompress_data():
    def decompress():
        try:
            with open("students.dat","rb") as file:
                compress_data = file.read()
            decompress_data = pickle.loads(zlib.decompress(compress_data))
            return decompress_data
        except FileNotFoundError:
            return None, None, None
        except Exception as e:
            return None, None, None
    threading.Thread(target=decompress).start()

def main():
    window = tk.Tk()
    window.title("Student Management System")

    students = []
    courses = []
    all_marks = []
    num_students = 0
    num_courses = 0

    #students, courses, all_marks = decompress_data()

    def do_exit():
        compress_data(students, courses, all_marks)
        window.destroy()

    def do_input_students():
        nonlocal num_students
        num_students = input_students(window)
    
    def do_input_courses():
        nonlocal num_courses
        num_courses = input_courses(window)

    def do_input_students_info():
        nonlocal students
        if num_students > 0:
            students = input_students_info(window, num_students)
        else:
            messagebox.showerror("Error", "You must input the number of students first.")

    def do_input_courses_info():
        nonlocal courses
        if num_courses > 0:
            courses = input_courses_info(window, num_courses)
        else:
            messagebox.showerror("Error", "You must input the number of courses first.")
    
    def do_input_marks():
        nonlocal all_marks
        if students and courses:
            course_id = simpledialog.askstring("Input marks", "Enter course id:")
            course = next((c for c in courses if c.id == course_id), None)
            if course:
                all_marks.append(input_marks(students, course, window))
            else:
                messagebox.showerror("Error", "Course ID is not found.")
        else:
            messagebox.showerror("Error", "You must input students and courses information first.")

    def do_display_students():
        if students:
            list_students(students, all_marks, window)
        else:
            messagebox.showerror("Error", "You must input students' information first.")

    def do_display_courses():
        if courses:
            list_courses(courses, window)
        else:
            messagebox.showerror("Error", "You must input courses' information first.")
    
    def do_gpa():
        if students and courses:
            gpa(students, all_marks, courses)
        else:
            messagebox.showerror("Error", "You must input students and courses information first.")

    button_exit = tk.Button(window, text="Exit", command = do_exit)
    button_exit.pack()
    button_input_students = tk.Button(window, text="Input number of students", command = do_input_students)
    button_input_students.pack()
    button_input_courses = tk.Button(window, text="Input number of courses", command = do_input_courses)
    button_input_courses.pack()
    button_input_students_info = tk.Button(window, text="Input students' information", command = do_input_students_info)
    button_input_students_info.pack()
    button_input_courses_info = tk.Button(window, text="Input courses' information", command = do_input_courses_info)
    button_input_courses_info.pack()
    button_input_marks = tk.Button(window, text="Input marks", command = do_input_marks)
    button_input_marks.pack()
    button_display_students = tk.Button(window, text="Display students' information", command = do_display_students)
    button_display_students.pack()
    button_display_courses = tk.Button(window, text="Display courses' information", command = do_display_courses)
    button_display_courses.pack()
    button_gpa = tk.Button(window, text="Sort Students by GPA", command=do_gpa)
    button_gpa.pack()
    window.mainloop()

if __name__ == "__main__":
    main()



