"""Lab 01.04 - Student Class (No Class)"""
def student():
    student1 = [input() for _ in range(5)]
    student2 = [input() for _ in range(5)]
    student3 = [input() for _ in range(5)]
    studentc = input()
    for i in [student1, student2, student3]:
        if studentc in i:
            gen = "Mr" if i[1] == "Male" else "Miss"
            gra = format(float(i[4]), ".2f")
            print(gen, i[0], "(" + i[2] + ")", "ID:", i[3], "GPA", gra)
            return
    print("Student not found")
student()
