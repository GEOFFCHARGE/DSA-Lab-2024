"""Exercise 01.02 - Elevator"""
class Elevator:

    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        if 1 <= floor <= self.max_floor:
            self.current_floor = floor
        else:
            print("Invalid Floor!")

    def report_current_floor(self):
        print(self.current_floor)

def main():
    status = Elevator(int(input()))
    while True:
        floor = input()
        if floor == "Done":
            status.report_current_floor()
            break
        status.go_to_floor(int(floor))
main()
