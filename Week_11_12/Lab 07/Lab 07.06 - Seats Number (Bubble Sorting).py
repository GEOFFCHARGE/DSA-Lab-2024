"""Labs 07.06 - Seats Number (Bubble Sorting)"""
import json
def bubbleSort(list, last):
    time = 0
    current = 0
    sorted = False
    while current <= last and not sorted:
        walker = last
        sorted = True
        while walker > current:
            if list[walker][0] < list[walker - 1][0] or \
                (list[walker][0] == list[walker - 1][0] and \
                int(list[walker][1:]) < int(list[walker - 1][1:])):
                sorted = False
                list[walker], list[walker - 1] = list[walker - 1], list[walker]
            time += 1
            walker -= 1
        print(list)
        current += 1
    print(f"Comparison times: {time}")

def main():
    bubbleSort(json.loads(input()), int(input()))
main()
