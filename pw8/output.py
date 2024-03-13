import curses
import math
import numpy as np


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
