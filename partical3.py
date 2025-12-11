

import math
import numpy as np
import curses


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
    def __init__(self, cid="", name="", credits=0):
        self.id = cid
        self.name = name
        self.credits = credits  

    def input(self):
        self.id = input("  ID: ")
        self.name = input("  Name: ")
        self.credits = int(input("  Credits: "))

    def list(self):
        print("ID:", self.id, "- Name:", self.name, "- Credits:", self.credits)


class MarkManager:
    def __init__(self):
        self.students = []        
        self.courses = []         
        self.marks = {}           
        self.gpas = {}             

    

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
            raw_mark = float(input(f"  Raw mark for student {s.id} - {s.name}: "))
           
            mark = math.floor(raw_mark * 10) / 10.0
            print(f"  => Stored mark (rounded down to 1 decimal): {mark}")
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

    

    def calculate_gpa_for_student(self, sid):
        
        credits = []
        marks = []

        for c in self.courses:
            key = (c.id, sid)
            if key in self.marks:
                credits.append(c.credits)
                marks.append(self.marks[key])

        if not credits:   
            return None

        credits_arr = np.array(credits)
        marks_arr = np.array(marks)

        
        gpa = np.sum(credits_arr * marks_arr) / np.sum(credits_arr)

        
        return round(float(gpa), 2)

    def calculate_all_gpas(self):
        self.gpas = {}
        for s in self.students:
            gpa = self.calculate_gpa_for_student(s.id)
            if gpa is not None:
                self.gpas[s.id] = gpa

    def show_gpa_for_student(self):
        if not self.students:
            print("No students.")
            return

        sid = input("Enter student ID to show GPA: ")

        
        student_found = False
        for s in self.students:
            if s.id == sid:
                student_found = True
                break

        if not student_found:
            print("Student not found.")
            return

        gpa = self.calculate_gpa_for_student(sid)
        if gpa is None:
            print("This student has no marks yet.")
        else:
            print(f"GPA for student {sid} - {s.name}: {gpa}")
        print()

    def list_students_sorted_by_gpa(self):
        if not self.students:
            print("No students.")
            return

        self.calculate_all_gpas()

        
        students_with_gpa = []
        for s in self.students:
            gpa = self.gpas.get(s.id, None)
            students_with_gpa.append((gpa, s))

        
        def sort_key(item):
            gpa, _ = item
            if gpa is None:
                return -1e9
            return gpa

        students_with_gpa.sort(key=sort_key, reverse=True)

        print("\n--- Students sorted by GPA (desc) ---")
        for gpa, s in students_with_gpa:
            if gpa is None:
                gpa_str = "N/A"
            else:
                gpa_str = f"{gpa:.2f}"
            print(f"ID: {s.id} - Name: {s.name} - GPA: {gpa_str}")
        print("-------------------------------------\n")

    

    def run(self):
        while True:
            print("===== STUDENT MARK MANAGEMENT (OOP + MATH + NUMPY) =====")
            print("1. Input students")
            print("2. Input courses")
            print("3. Select a course and input marks")
            print("4. List students")
            print("5. List courses")
            print("6. Show student marks for a course")
            print("7. Show GPA for a student")
            print("8. List students sorted by GPA (desc)")
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
            elif choice == "7":
                self.show_gpa_for_student()
            elif choice == "8":
                self.list_students_sorted_by_gpa()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.\n")



def show_banner_curses():
    
    def _inner(stdscr):
        curses.curs_set(0)
        stdscr.clear()

        text1 = "STUDENT MARK MANAGEMENT"
        text2 = "Practical 3 - math, numpy & curses"
        h, w = stdscr.getmaxyx()
        x1 = (w - len(text1)) // 2
        x2 = (w - len(text2)) // 2
        y = h // 2 - 1

        stdscr.addstr(y,     x1, text1, curses.A_BOLD)
        stdscr.addstr(y + 1, x2, text2)
        stdscr.addstr(y + 3, x2, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()

    curses.wrapper(_inner)


def main():
    
    try:
        show_banner_curses()
    except Exception:
        
        pass

    manager = MarkManager()
    manager.run()


if __name__ == "__main__":
    main()
