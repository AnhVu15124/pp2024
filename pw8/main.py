import curses
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

def main(stdscr):
    courses = []
    students = []
    all_marks = []
    num_students = 0
    num_courses = 0

    #students, courses, all_marks = decompress_data()

    while True:
        stdscr.clear()
        stdscr.addstr("""
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
            stdscr.addstr("Exiting...")
            stdscr.refresh()
            curses.napms(1000)
            compress_data(students, courses, all_marks)
            break
        elif option == ord('1'):
            num_students = input_students(stdscr)
        elif option == ord('2'):
            num_courses = input_courses(stdscr)
        elif option == ord('3'):
            if num_students > 0:
                students = input_student_infos(stdscr, num_students)
            else:
                stdscr.addstr("You must input number of students first.")
                stdscr.getch()  
        elif option == ord('4'):
            if num_courses > 0:
                courses = input_course_infos(stdscr, num_courses)
            else:
                stdscr.addstr("You must input number of courses first.")
                stdscr.getch()  
        elif option == ord('5'):
            if students and courses:
                stdscr.addstr("Enter course id: ")
                stdscr.refresh()
                course_id = stdscr.getstr().decode()
                course = next((c for c in courses if c.id == course_id), None)
                if course:
                    all_marks.append(input_marks(course, students, stdscr))
                else:
                    stdscr.addstr("Id is not found.")
                    stdscr.getch()  
            else:
                stdscr.addstr("You must input both students and courses information first.")
                stdscr.getch()  
        elif option == ord('6'):
            if students:
                list_students(students, all_marks, stdscr)
            else:
                stdscr.addstr("You must input students' information first.")
                stdscr.getch()  
        elif option == ord('7'):
            if courses:
                list_courses(courses, stdscr)
            else:
                stdscr.addstr("You must input courses' information first.")
                stdscr.getch()  
        elif option == ord('8'):
            if students:
                sorted_students = gpa(students, all_marks, courses)
                stdscr.addstr("Students' information sorted by GPA:")
                stdscr.refresh()
                stdscr.getch()  
                for student, gpa_value in sorted_students:
                    student.display_info(stdscr)
                    stdscr.addstr(f"GPA: {gpa_value:.1f}")
                    stdscr.refresh()
                    stdscr.getch()  
            else:
                stdscr.addstr("You must input courses information first.")
                stdscr.getch()  
        else:
            stdscr.addstr("Please try again!")
            stdscr.getch()  

    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)

