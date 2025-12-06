

class Student:
    def __init__(self, sid="", name="", dob=""):
        self.id = sid
        self.name = name
        self.dob = dob

    def input(self):
        self.id = input("  ID: ")
        self.name = input("  Name: ")
        self.dob = input("  Date of birth: ")

    def list(self):
        print("ID:", self.id, "- Name:", self.name, "- DoB:", self.dob)


class Course:
    def __init__(self, cid="", name=""):
        self.id = cid
        self.name = name

    def input(self):
        self.id = input("  ID: ")
        self.name = input("  Name: ")

    def list(self):
        print("ID:", self.id, "- Name:", self.name)


class MarkManager:
    def __init__(self):
       
        self.students = []      
        self.courses = []       
        self.marks = {}         

    
    def input_number_of_students(self):
        n = int(input("Enter number of students in class: "))
        return n

    def input_students(self):
        n = self.input_number_of_students()
        for i in range(n):
            print("\nStudent", i + 1)
            s = Student()
            s.input()        
            self.students.append(s)

    def list_students(self):
        print("\n--- Student list ---")
        for s in self.students:
            s.list()         
        print("--------------------\n")

   
    def input_number_of_courses(self):
        n = int(input("Enter number of courses: "))
        return n

    def input_courses(self):
        n = self.input_number_of_courses()
        for i in range(n):
            print("\nCourse", i + 1)
            c = Course()
            c.input()
            self.courses.append(c)

    def list_courses(self):
        print("\n--- Course list ---")
        for c in self.courses:
            c.list()
        print("-------------------\n")

    
    def select_course_and_input_marks(self):
        if not self.courses:
            print("No courses. Please input courses first.")
            return
        if not self.students:
            print("No students. Please input students first.")
            return

        print("\nAvailable courses:")
        for c in self.courses:
            print("  ", c.id, "-", c.name)

        cid = input("Enter course ID to input marks: ")

       
        course_found = False
        for c in self.courses:
            if c.id == cid:
                course_found = True
                break

        if not course_found:
            print("Course not found.")
            return

        print("\nInput marks for course:", cid)
        for s in self.students:
            mark = float(input(f"  Mark for student {s.id} - {s.name}: "))
            self.marks[(cid, s.id)] = mark

    def show_marks_for_course(self):
        if not self.courses:
            print("No courses.")
            return

        cid = input("Enter course ID to show marks: ")

        print("\nMarks for course:", cid)
        found_any = False
        for s in self.students:
            key = (cid, s.id)
            if key in self.marks:
                print("Student", s.id, "-", s.name, ":", self.marks[key])
                found_any = True

        if not found_any:
            print("No marks recorded for this course yet.")
        print()

    
    def run(self):
        while True:
            print("===== STUDENT MARK MANAGEMENT (OOP) =====")
            print("1. Input students")
            print("2. Input courses")
            print("3. Select a course and input marks")
            print("4. List students")
            print("5. List courses")
            print("6. Show student marks for a course")
            print("0. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.select_course_and_input_marks()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                self.list_courses()
            elif choice == "6":
                self.show_marks_for_course()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.\n")


def main():
    manager = MarkManager()
    manager.run()


if __name__ == "__main__":
    main()
