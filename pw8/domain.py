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
