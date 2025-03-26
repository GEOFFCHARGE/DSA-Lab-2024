"""Labs 07.05 - Seats Number (Selection Sorting)"""
import json
def selectionSort(list, last):
    time = 0
    current = 0
    while current < last:
        smallest = current
        walker = current + 1
        while walker <= last:
            if list[walker][0] < list[smallest][0] or \
                (list[walker][0] == list[smallest][0] and \
                int(list[walker][1:]) < int(list[smallest][1:])):
                smallest = walker
            time += 1
            walker += 1
        list[current], list[smallest] = list[smallest], list[current]
        print(list)
        current += 1
    print(f"Comparison times: {time}")

def main():
    selectionSort(json.loads(input()), int(input()))
main()
