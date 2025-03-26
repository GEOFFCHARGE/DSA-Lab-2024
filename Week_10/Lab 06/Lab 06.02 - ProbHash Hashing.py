"""Lab 06.02 - ProbHash Hashing"""
class Student:

    def __init__(self, std_id, name, gpa):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        return self.std_id

    def get_name(self):
        return self.name

    def get_gpa(self):
        return f"{self.gpa:.02f}"

    def print_details(self):
        print(f"ID: {self.get_std_id()}\nName: {self.get_name()}\nGPA: {self.get_gpa()}")

class ProbHash:

    def __init__(self, size):
        self.hash_table = [None] * size
        self.size = size

    def hash(self, key):
        return key % self.size

    def rehash(self, hkey):
        return (hkey + 1) % self.size

    def insert_data(self, student):
        value = self.hash(student.get_std_id())
        index = value
        while True:
            if not self.hash_table[index]:
                self.hash_table[index] = student
                print(f"Insert {student.get_std_id()} at index {index}")
                break
            index = self.rehash(index)
            if index == value:
                print(f"The list is full. {student.get_std_id()} could not be inserted.")
                break

    def search_data(self, std_id):
        for index, value in enumerate(self.hash_table):
            if value and value.get_std_id() == std_id:
                print(f"Found {std_id} at index {index}")
                return value
        print(f"{std_id} does not exist.")
        return

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
