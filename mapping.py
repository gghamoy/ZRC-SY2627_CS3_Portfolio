class Student:
    def __init__(self, studentID, studentName):
        self.studentID = studentID
        self.studentName = studentName


class Course:
    def __init__(self, courseCode, courseName):
        self.courseCode = courseCode
        self.courseName = courseName
        self.students = []

    def addStudent(self, student):
        self.students.append(student)


student1 = Student("S001", "John")
student2 = Student("S002", "Maria")

course1 = Course("CS101", "Computer Science")

course1.addStudent(student1)
course1.addStudent(student2)

for student in course1.students:
    print(student.studentID, student.studentName)
