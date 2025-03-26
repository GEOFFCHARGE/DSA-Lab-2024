"""Labs 07.04 - Seats Number (Insertion Sorting)"""
import json
def insertionSort(list, last):
    time = 0
    current = 1
    while current <= last:
        hold = list[current]
        walker = current - 1
        while walker >= 0 and hold[0] < list[walker][0] or \
            (hold[0] == list[walker][0] and int(hold[1:]) < int(list[walker][1:])):
            list[walker + 1] = list[walker]
            walker -= 1
            time += 1
        list[walker + 1] = hold
        if walker >= 0:
            time += 1
        print(list)
        current += 1
    print(f"Comparison times: {time}")

def main():
    insertionSort(json.loads(input()), int(input()))
main()
