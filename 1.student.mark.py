def input_students():
    num_students = input("Enter the number of students in this class: ")
    if num_students.isnumeric()==False:
        print("The number of students must be a positive number")
        return 0
    else:
        num_students = int(num_students)
        if num_students > 0:
            return num_students
        else:
            print("The number of students must be a positive number")
            return 0

def input_course():
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
    students = {}
    for i in range(num_students):
        print("_________________________________________________________________")
        id = input(f"Enter student {i+1} id: ")
        name = input(f"Enter student {i+1} name: ")
        dob = input(f"Enter student {i+1} date of birth(dd/mm/yyyy): ")
        students[id] = {"name": name, "dob": dob}

    return students

def input_course_infos(num_courses):
    courses = {}
    for i in range(num_courses):
        print("_________________________________________________________________")
        id = input(f"Enter course {i+1} id: ")
        name = input(f"Enter course {i+1} name: ")
        courses[id] = {"name": name}

    return courses

def input_mark(students, courses):
    course_id = input("Enter course id: ")
    if course_id not in courses:
        print("Id is not found")
        return None, None

    marks = {}
    for student_id in students:
        mark = input(f"Enter mark for student {student_id}: ")
        marks[student_id] = mark

    return course_id, marks

def list_students(students, all_marks):
   print("Students' information")
   for id, info in students.items():
    print(f"""_________________________________________________________________
ID: {id}
Name: {info["name"]}
Date of birth: {info["dob"]}""")
    for course_id, marks in all_marks.items():
        if id in marks:
            print(f"Mark for course {course_id} is {marks[id]}")

def list_courses(courses):
    print("Courses' information")
    for id, info in courses.items():
        print(f"""_________________________________________________________________
ID: {id}
Name: {info["name"]}""")
def main():
    courses = {}
    students = {}
    all_marks = {}
    num_students = 0
    num_courses = 0

    while(True):
        print("""
_________________________________________________________________
1. Input number of students
2. Input number of courses
3. Input students' information
4. Input courses' information
5. Input students' mark for courses
6. Display students' information
7. Display courses' information
0. Exit
_________________________________________________________________
    """)
        option = (input("Your choice: "))                                                         
        if option == '0':
            print("Exiting...")
            break

        elif option == '1':                                                                          
            num_students = input_students()
        elif option == '2':                                                                                                                               
            num_courses = input_course()
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
                course_id, marks = input_mark(students, courses)
                all_marks[course_id] = marks
            else:
                print("You must input both students and courses infomation first")
        elif option == '6':
            if students:
                list_students(students, all_marks)
            else:
                print("You must input students infomation first")
        elif option == '7':
            if courses:
                list_courses(courses)
            else:
                print("You must input courses infomation first")
               
        else:
            print("Please try again!")

if __name__ == "__main__":
    main()
