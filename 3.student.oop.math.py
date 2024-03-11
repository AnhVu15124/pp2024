import curses
import math
import numpy as np

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def display_info(self, stdscr):
        stdscr.addstr("_________________________________________________________________\n")
        stdscr.addstr(f"ID: {self.id}\nName: {self.name}\nDate of birth: {self.dob}\n")

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

    def display_info(self, stdscr):
        stdscr.addstr("_________________________________________________________________\n")
        stdscr.addstr(f"ID: {self.id}\nName: {self.name}\nCredit: {self.credit}\n")


class All_marks:
    def __init__(self):
        self.course = None
        self.marks = {}

    def input_mark(self, students, stdscr):
        for student in students:
            stdscr.addstr(f"Enter mark for student {student.id}: ")
            stdscr.refresh()
            mark = stdscr.getstr(0, 0, 5).decode()
            mark = float(mark)
            mark = math.floor(mark * 10) / 10
            self.marks[student.id] = mark


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
        students.append(Student(id, name, dob))
    return students


def input_course_infos(stdscr, num_courses):
    courses = []
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
        courses.append(Course(id, name, credit))
    return courses


def input_marks(course, students, stdscr):
    all_mark = All_marks()
    all_mark.course = course
    all_mark.input_mark(students, stdscr)
    return all_mark


def list_students(students, all_marks, stdscr):
    stdscr.addstr("Students' information\n")
    for student in students:
        student.display_info(stdscr)
        for all_mark in all_marks:
            if student.id in all_mark.marks:
                stdscr.addstr(f"Mark for course {all_mark.course.id} is {all_mark.marks[student.id]}\n")

def gpa(students, all_marks, courses):
    student_gpas = []
    for student in students:
        marks = np.array([all_mark.marks[student.id] for all_mark in all_marks if student.id in all_mark.marks])
        course_ids = [all_mark.course.id for all_mark in all_marks if student.id in all_mark.marks]
        credits = np.array([course.credit for course in courses if course.id in course_ids])
        total_grade_points = np.sum(marks * credits)
        total_credits = np.sum(credits)
        gpa = total_grade_points / total_credits
        student_gpas.append((student, gpa))

    sorted_students = sorted(student_gpas, key=lambda x: x[1], reverse=True)
    return sorted_students


def list_courses(courses, stdscr):
    stdscr.addstr("Courses' information\n")
    for course in courses:
        course.display_info(stdscr)

def main(stdscr):
    courses = []
    students = []
    all_marks = []
    num_students = 0
    num_courses = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, """
__________________________________________________________________
1. Input number of students
2. Input number of courses
3. Input students' information
4. Input courses' information
5. Input students' mark for courses
6. Display students' information
7. Display courses' information
8. Sort students by GPA
0. Exit
__________________________________________________________________
""")
        stdscr.refresh()

        option = stdscr.getch()

        if option == ord('0'):
            stdscr.addstr(0, 0, "Exiting...")
            stdscr.refresh()
            curses.napms(1000)
            break
        elif option == ord('1'):
            num_students = input_students(stdscr)
        elif option == ord('2'):
            num_courses = input_courses(stdscr)
        elif option == ord('3'):
            if num_students > 0:
                students = input_student_infos(stdscr, num_students)
            else:
                stdscr.addstr(0, 0, "You must input number of students first.")
                stdscr.getch()  
        elif option == ord('4'):
            if num_courses > 0:
                courses = input_course_infos(stdscr, num_courses)
            else:
                stdscr.addstr(0, 0, "You must input number of courses first.")
                stdscr.getch()  
        elif option == ord('5'):
            if students and courses:
                stdscr.addstr("Enter course id: ")
                stdscr.refresh()
                course_id = stdscr.getstr(0, 0, 50).decode()
                course = next((c for c in courses if c.id == course_id), None)
                if course:
                    all_marks.append(input_marks(course, students, stdscr))
                else:
                    stdscr.addstr(0, 0, "Id is not found.")
                    stdscr.getch()  
            else:
                stdscr.addstr(0, 0, "You must input both students and courses information first.")
                stdscr.getch()  
        elif option == ord('6'):
            if students:
                list_students(students, all_marks, stdscr)
            else:
                stdscr.addstr(0, 0, "You must input students' information first.")
                stdscr.getch()  
        elif option == ord('7'):
            if courses:
                list_courses(courses, stdscr)
            else:
                stdscr.addstr(0, 0, "You must input courses' information first.")
                stdscr.getch()  
        elif option == ord('8'):
            if students:
                sorted_students = gpa(students, all_marks, courses)
                stdscr.addstr(0, 0, "Students' information sorted by GPA:")
                stdscr.refresh()
                stdscr.getch()  
                for student, gpa_value in sorted_students:
                    student.display_info(stdscr)
                    stdscr.addstr(f"GPA: {gpa_value:.1f}")
                    stdscr.refresh()
                    stdscr.getch()  
            else:
                stdscr.addstr(0, 0, "You must input courses information first.")
                stdscr.getch()  
        else:
            stdscr.addstr(0, 0, "Please try again!")
            stdscr.getch()  

    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
