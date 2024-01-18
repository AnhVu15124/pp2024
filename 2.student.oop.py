class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def display_info(self):
        print("_________________________________________________________________")
        print(f"ID: {self.id}\nName: {self.name}\nDate of birth: {self.dob}")

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display_info(self):
        print("_________________________________________________________________")
        print(f"ID: {self.id}\nName: {self.name}")


class All_marks:
    def __init__(self):
        self.course = None
        self.marks = {}
    def input_mark(self, students):
        for student in students:
            mark = input(f"Enter mark for student {student.id}: ")
            self.marks[student.id] = mark
            

def input_students():
    num_students = input("Enter the number of students in this class: ")
    if not num_students.isnumeric():
        print("The number of students must be a positive number")
        return 0
    else:
        num_students = int(num_students)
        if num_students > 0:
            return num_students
        else:
            print("The number of students must be a positive number")
            return 0

def input_courses():
    num_courses = input("Enter the number of courses in this class: ")
    if num_courses.isnumeric()==False:
        print("The number of courses must be a positive number")
        return 0
    else:
        num_courses = int(num_courses)
        if num_courses > 0:
            return num_courses
        else:
            print("The number of courses must be a positive number")
            return 0

        
def input_student_infos(num_students):
    students = []
    for i in range(num_students):
            print("_________________________________________________________________")
            id = input(f"Enter student {i+1} id: ")
            name = input(f"Enter student {i+1} name: ")
            dob = input(f"Enter student {i+1} date of birth(dd/mm/yyyy): ")
            students.append(Student(id, name, dob))     
    return students


def input_course_infos(num_courses):
    courses = []
    for i in range(num_courses):
            print("_________________________________________________________________")
            id = input(f"Enter course {i+1} id: ")
            name = input(f"Enter course {i+1} name: ")
            courses.append(Course(id, name))     
    return courses


def input_marks(course, students):
    all_mark = All_marks()
    all_mark.course = course
    all_mark.input_mark(students)
    return all_mark


def list_students(students, all_marks):
    print("Students' information")
    for student in students:
        student.display_info()
        for all_mark in all_marks:
            if student.id in all_mark.marks:
                print(f"Mark for course {all_mark.course.id} is {all_mark.marks[student.id]}")


def list_courses(courses):
    print("Courses' information")
    for course in courses:
        course.display_info()


def main():
    courses = []
    students = []
    all_marks = []
    num_students = 0
    num_courses = 0


    while (True):
        print("""
__________________________________________________________________
1. Input number of students
2. Input number of courses
3. Input students' information
4. Input courses' information
5. Input students' mark for courses
6. Display students' information
7. Display courses' information
0. Exit
__________________________________________________________________
""")
        option = input("Your choice: ")

        if option == '0':
            print("Exiting...")
            break
        elif option == '1':
            num_students = input_students()
        elif option == '2':
            num_courses = input_courses()
        elif option == '3':
            if num_students > 0:
                students = input_student_infos(num_students)
            else:
                print("You must input number of students first")
        elif option == '4':
            if num_courses > 0:
                courses = input_course_infos(num_courses)
            else:
                print("You must input number of courses first")
        elif option == '5':
            if students and courses:
                course_id = input("Enter course id: ")
                course = next((c for c in courses if c.id == course_id), None)
                if course:
                    all_marks.append(input_marks(course, students))
                else:
                    print("Id is not found")
            else:
                print("You must input both students and courses information first")
        elif option == '6':
            if students:
                list_students(students, all_marks)
            else:
                print("You must input both students information first")
        elif option == '7':
            if courses:
                list_courses(courses)
            else:
                print("You must input courses information first")
        else:
            print("Please try again!")


if __name__ == "__main__":
    main()
