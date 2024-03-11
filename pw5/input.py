import curses
import math
from domain import Student, Course, All_marks

def input_students(stdscr):
    stdscr.addstr("Enter the number of students in this class: ")
    stdscr.refresh()
    num_students = stdscr.getstr(0, 0, 5).decode()
    if not num_students.isnumeric():
        stdscr.addstr("The number of students must be a positive number\n")
        stdscr.refresh()
        stdscr.getch()
        return 0
    else:
        num_students = int(num_students)
        if num_students > 0:
            return num_students
        else:
            stdscr.addstr("The number of students must be a positive number\n")
            stdscr.refresh()
            stdscr.getch()
            return 0

def input_courses(stdscr):
    stdscr.addstr("Enter the number of courses in this class: ")
    stdscr.refresh()
    num_courses = stdscr.getstr(0, 0, 5).decode()
    if not num_courses.isnumeric():
        stdscr.addstr("The number of courses must be a positive number\n")
        stdscr.refresh()
        stdscr.getch()
        return 0
    else:
        num_courses = int(num_courses)
        if num_courses > 0:
            return num_courses
        else:
            stdscr.addstr("The number of courses must be a positive number\n")
            stdscr.refresh()
            stdscr.getch()
            return 0

        
def input_student_infos(stdscr, num_students):
    students = []
    with open("students.txt","w") as file:
        for i in range(num_students):
            stdscr.addstr("_________________________________________________________________\n")
            stdscr.addstr(f"Enter student {i+1} id: ")
            stdscr.refresh()
            id = stdscr.getstr(0, 0, 50).decode()
            stdscr.addstr(f"Enter student {i+1} name: ")
            stdscr.refresh()
            name = stdscr.getstr(0, 0, 50).decode()
            stdscr.addstr(f"Enter student {i+1} date of birth (dd/mm/yyyy): ")
            stdscr.refresh()
            dob = stdscr.getstr(0, 0, 50).decode()
            student = Student(id, name, dob)
            students.append(student)
            file.write(f"ID: {student.id}\nName: {student.name}\nDate of birth: {student.dob}\n_________________________________________________________________\n")
    return students


def input_course_infos(stdscr, num_courses):
    courses = []
    with open("courses.txt","w") as file:
        for i in range(num_courses):
            stdscr.addstr("_________________________________________________________________\n")
            stdscr.addstr(f"Enter course {i+1} id: ")
            stdscr.refresh()
            id = stdscr.getstr(0, 0, 50).decode()
            stdscr.addstr(f"Enter course {i+1} name: ")
            stdscr.refresh()
            name = stdscr.getstr(0, 0, 50).decode()
            stdscr.addstr(f"Enter course {i+1} credit: ")
            stdscr.refresh()
            credit = int(stdscr.getstr(0, 0, 50).decode())
            course = Course(id, name, credit)
            courses.append(course)
            file.write(f"ID: {course.id}\nName: {course.name}\nCredit: {course.credit}\n_________________________________________________________________\n")
    return courses


def input_marks(course, students, stdscr):
    all_mark = All_marks()
    all_mark.course = course
    all_mark.input_mark(students, stdscr)

    with open("marks.txt","a") as file:
        for student in students:
            if student.id in all_mark.marks:
                file.write(f"Student ID: {student.id}\nCourse ID: {course.id}\nMark: {all_mark.marks[student.id]}\n_________________________________________________________________\n")
    return all_mark
