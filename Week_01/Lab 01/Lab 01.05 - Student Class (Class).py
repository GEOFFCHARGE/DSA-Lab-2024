"""Lab 01.05 - Student Class (Class)"""
class Student:

    def __init__(self, name, gend, ages, idst, grad):
        self.name = name
        self.gend = gend
        self.ages = ages
        self.idst = idst
        self.grad = grad

def main():
    student1 = Student(input(), input(), input(), input(), input())
    student2 = Student(input(), input(), input(), input(), input())
    student3 = Student(input(), input(), input(), input(), input())
    studentc = input()
    sta = ""
    for i in [student1, student2, student3]:
        if i.idst == studentc:
            gen = "Mr" if i.gend == "Male" else "Miss"
            sta = f"{gen} {i.name} ({i.ages}) ID: {i.idst} GPA {float(i.grad):.2f}"
    if not sta:
        print("Student not found")
    else:
        print(sta)
main()
