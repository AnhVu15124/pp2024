def input_students():
    return int(input("Enter the number of students in this class: "))

def input_course():
    return int(input("Enter the number of courses in this class: "))

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
        print("Id not found")
        return None, None

    marks = {}
    for student_id in students:
        mark = input(f"Enter mark for student {student_id}: ")
        marks[student_id] = mark

    return course_id, marks

def list_students(students, marks):

   for id, info in students.items():
    print(f"""_________________________________________________________________
ID: {id}
Name: {info["name"]}
Date of birth: {info["dob"]}""")

def list_courses(courses):
    # TODO: check what happens if there's no course (hint: len(course))
    print("There aren't any courses yet")
        
    print("Here is the course list: ")
    # TODO: add loop function to check the info of course
    print(f"{i+1}. {course['id']} - {course['name']}")

def main():
    courses = {}
    students = {}
    marks = {}
    num_students = 0
    num_courses = 0

    while(True):
        print("""_________________________________________________________________
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
            students = input_student_infos(num_students)
        elif option == '4':
            courses = input_course_infos(num_courses)
        elif option == '5':
            course_id, marks = input_mark(students, courses)
        elif option == '6':
            list_students(students, marks)
               
        else:
            print("Invalid input. Please try again!")

if _name_ == "_main_":
    main()
