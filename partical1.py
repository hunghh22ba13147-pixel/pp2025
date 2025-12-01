students = []   
courses = []   
marks = {}      
def input_number_of_students():
    n = int(input("Enter number of students in class: "))
    return n


def input_students(n):
    for i in range(n):
        print("\nStudent", i + 1)
        sid = input("  ID: ")
        name = input("  Name: ")
        dob = input("  Date of birth: ")
        students.append({"id": sid, "name": name, "dob": dob})


def input_number_of_courses():
    n = int(input("Enter number of courses: "))
    return n


def input_courses(n):
    for i in range(n):
        print("\nCourse", i + 1)
        cid = input("  ID: ")
        name = input("  Name: ")
        courses.append({"id": cid, "name": name})


def select_course_and_input_marks():
    if not courses:
        print("No courses. Please input courses first.")
        return
    if not students:
        print("No students. Please input students first.")
        return

    print("\nAvailable courses:")
    for c in courses:
        print("  ", c["id"], "-", c["name"])

    cid = input("Enter course ID to input marks: ")

    # check course exists
    course_found = False
    for c in courses:
        if c["id"] == cid:
            course_found = True
            break

    if not course_found:
        print("Course not found.")
        return

    print("\nInput marks for course:", cid)
    for s in students:
        mark = float(input(f"  Mark for student {s['id']} - {s['name']}: "))
        marks[(cid, s["id"])] = mark


def list_courses():
    print("\n--- Course list ---")
    for c in courses:
        print("ID:", c["id"], "- Name:", c["name"])
    print("-------------------\n")


def list_students():
    print("\n--- Student list ---")
    for s in students:
        print("ID:", s["id"], "- Name:", s["name"], "- DoB:", s["dob"])
    print("--------------------\n")


def show_marks_for_course():
    if not courses:
        print("No courses.")
        return

    cid = input("Enter course ID to show marks: ")

    print("\nMarks for course:", cid)
    found_any = False
    for s in students:
        key = (cid, s["id"])
        if key in marks:
            print("Student", s["id"], "-", s["name"], ":", marks[key])
            found_any = True

    if not found_any:
        print("No marks recorded for this course yet.")
    print()


def main():
    while True:
        print("===== STUDENT MARK MANAGEMENT =====")
        print("1. Input students")
        print("2. Input courses")
        print("3. Select a course and input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            n = input_number_of_students()
            input_students(n)
        elif choice == "2":
            n = input_number_of_courses()
            input_courses(n)
        elif choice == "3":
            select_course_and_input_marks()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_marks_for_course()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
