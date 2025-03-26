"""Lab 06.03 - Binary Search"""

class Student:

    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_gpa(self):
        return f"{self.gpa:.02f}"

    def print_details(self):
        return f"ID: {self.get_id()}\nName: {self.get_name()}\nGPA: {self.get_gpa()}"

class BinarySearch:

    def __init__(self, data, size):
        self.list = data
        self.size = size

    def search_data(self, name):
        rounds = 0
        begins = 0
        lasted = self.size - 1
        while begins <= lasted:
            rounds += 1
            middle = (begins + lasted) // 2
            if self.list[middle].get_name() < name:
                begins = middle + 1
            elif self.list[middle].get_name() > name:
                lasted = middle - 1
            else:
                print(f"Found {name} at index {middle}\n{self.list[middle].print_details()}\nComparisons times: {rounds}")
                return
        print(f"{name} does not exists.\nComparisons times: {rounds}")

import json
def main():
    data = [Student(i["id"], i["name"], i["gpa"]) for i in json.loads(input())]
    name = input()
    stdn = BinarySearch(data, len(data))
    stdn.search_data(name)
main()
