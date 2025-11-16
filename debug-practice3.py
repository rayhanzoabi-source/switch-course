import random
from datetime import datetime, timedelta

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []
        self.grades = {}
        self.attendance = {} 

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            self.grades[course] = []
            course.add_student(self)
            print(f"{self.name} enrolled in {course.name}")
        else:
            print(f"{self.name} is already enrolled in {course.name}")

    def assign_grade(self, course, grade):
        if course in self.courses:
            self.grades[course].append(grade)
            print(f"Grade {grade} assigned to {self.name} for {course.name}")
        else:
            print(f"{self.name} is not enrolled in {course.name}")

    def calculate_gpa(self):
        if not self.grades:
            return 0
        total_grade = sum(sum(grades) for grades in self.grades.values())
        total_courses = sum(len(grades) for grades in self.grades.values())
        return total_grade / total_courses if total_courses > 0 else 0
    

    def record_attendance(self, course, date, present):
        if course not in self.attendance:
            self.attendance[course] = {}
        self.attendance[course][date] = present

class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.courses = []

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.assign_teacher(self)
            print(f"{self.name} assigned to teach {course.name}")
        else:
            print(f"{self.name} is already teaching {course.name}")

class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id
        self.teacher = None
        self.students = []
        self.schedule = []

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def add_schedule(self, day, time):
        self.schedule.append((day, time))
    
    def get_average_grade(self):
        if not self.students:
            return 0
        total_grades = sum(sum(student.grades[self]) for student in self.students)
        total_grades_count = sum(len(student.grades[self]) for student in self.students)
        return total_grades / total_grades_count if total_grades_count > 0 else 0

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to {self.name}")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Teacher {teacher.name} added to {self.name}")

    def add_course(self, course):
        self.courses.append(course)
        print(f"Course {course.name} added to {self.name}")

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def get_teacher_by_id(self, employee_id):
        for teacher in self.teachers:
            if teacher.employee_id == employee_id:
                return teacher
        return None

    def get_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None
    
    def get_students_with_failed_grades(fail_threshold=60):
        failed_students = []
        for student in self.students:
            for course, grades in student.grades.items():
                if any(grade < fail_threshold for grade in grades):
                    failed_students.append((student, course))
                    break  # We only need to add the student once
        return failed_students

    def get_top_performing_students(self, top_n=5):
        students_with_gpa = [(student, student.calculate_gpa()) for student in self.students]
        return sorted(students_with_gpa, key=lambda x: x[1], reverse=True)[:top_n]

    def get_courses_with_highest_average_grades(self, top_n=3):
        courses_with_avg = [(course, course.get_average_grade()) for course in self.courses]
        return sorted(courses_with_avg, key=lambda x: x[1], reverse=True)[:top_n]

    def get_teachers_with_most_students(self, top_n=3):
        teacher_student_count = [(teacher, sum(len(course.students) for course in teacher.courses)) for teacher in self.teachers]
        return sorted(teacher_student_count, key=lambda x: x[1], reverse=True)[:top_n]

    def get_students_with_perfect_attendance(self):
        perfect_attendance = []
        for student in self.students:
            has_perfect_attendance = all(all(present for present in course_attendance.values()) 
                                         for course_attendance in student.attendance.values())
            if has_perfect_attendance:
                perfect_attendance.append(student)
        return perfect_attendance

def generate_demo_data(school):
    # Generate Students
    for i in range(1, 51):
        student = Student(f"Student {i}", random.randint(18, 25), f"S{1000+i}")
        school.add_student(student)

    # Generate Teachers
    for i in range(1, 11):
        teacher = Teacher(f"Teacher {i}", random.randint(30, 60), f"T{100+i}")
        school.add_teacher(teacher)

    # Generate Courses
    courses = [
        "Mathematics", "Physics", "Chemistry", "Biology", "Computer Science",
        "Literature", "History", "Geography", "Art", "Music"
    ]
    for i, course_name in enumerate(courses, 1):
        course = Course(course_name, f"C{100+i}")
        school.add_course(course)
        
        # Assign a random teacher to the course
        teacher = random.choice(school.teachers)
        teacher.assign_course(course)
        
        # Add a random schedule
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        times = ["09:00", "11:00", "14:00", "16:00"]
        for _ in range(2):  # Two classes per week
            course.add_schedule(random.choice(days), random.choice(times))

    # Enroll students in random courses
    for student in school.students:
        num_courses = random.randint(3, 5)
        for _ in range(num_courses):
            course = random.choice(school.courses)
            student.enroll(course)

    # Assign random grades
    for student in school.students:
        for course in student.courses:
            for _ in range(3):  # 3 grades per course
                grade = random.randint(40, 100)
                student.assign_grade(course, grade)

    
    # Generate attendance data
    start_date = datetime.now() - timedelta(days=30)
    for _ in range(30):
        current_date = start_date + timedelta(days=_)
        for student in school.students:
            for course in student.courses:
                student.record_attendance(course, current_date, random.choice([True, True, True, False]))  # 75% chance of being present


def print_school_stats(school):
    print(f"\n--- {school.name} Statistics ---")
    print(f"Total Students: {len(school.students)}")
    print(f"Total Teachers: {len(school.teachers)}")
    print(f"Total Courses: {len(school.courses)}")
    
    # Average GPA
    total_gpa = sum(student.calculate_gpa() for student in school.students)
    avg_gpa = total_gpa / len(school.students) if school.students else 0
    print(f"Average GPA: {avg_gpa:.2f}")
    
    # Most popular course
    course_popularity = {course: len(course.students) for course in school.courses}
    most_popular = max(course_popularity, key=course_popularity.get)
    print(f"Most Popular Course: {most_popular.name} ({course_popularity[most_popular]} students)")

    # print_school_stats(school):
    print(f"\n--- {school.name} Statistics ---")
    print(f"Total Students: {len(school.students)}")
    print(f"Total Teachers: {len(school.teachers)}")
    print(f"Total Courses: {len(school.courses)}")
    
    # Average GPA
    total_gpa = sum(student.calculate_gpa() for student in school.students)
    avg_gpa = total_gpa / len(school.students) if school.students else 0
    print(f"Average GPA: {avg_gpa:.2f}")
    
    # Most popular course
    course_popularity = {course: len(course.students) for course in school.courses}
    most_popular = max(course_popularity, key=course_popularity.get)
    print(f"Most Popular Course: {most_popular.name} ({course_popularity[most_popular]} students)")
    
    # Top 3 performing students
    print("\nTop 3 Performing Students:")
    top_students = school.get_top_performing_students(3)
    for i, (student, gpa) in enumerate(top_students, 1):
        print(f"{i}. {student.name} (ID: {student.student_id}) - GPA: {gpa:.2f}")

    # Top 3 courses with highest average grades
    print("\nTop 3 Courses with Highest Average Grades:")
    top_courses = school.get_courses_with_highest_average_grades(3)
    for i, (course, avg_grade) in enumerate(top_courses, 1):
        print(f"{i}. {course.name} - Average Grade: {avg_grade:.2f}")

    # Top 3 teachers with most students
    print("\nTop 3 Teachers with Most Students:")
    top_teachers = school.get_teachers_with_most_students(3)
    for i, (teacher, student_count) in enumerate(top_teachers, 1):
        print(f"{i}. {teacher.name} - Total Students: {student_count}")

    # Students with perfect attendance
    perfect_attendance = school.get_students_with_perfect_attendance()
    print(f"\nNumber of Students with Perfect Attendance: {len(perfect_attendance)}")

    # Students with failed grades
    failed_students = school.get_students_with_failed_grades(50)
    print(f"\nNumber of Students with Failed Grades: {len(failed_students)}")



if __name__ == "__main__":
    school = School("Python High School")
    generate_demo_data(school)
    print_school_stats(school)