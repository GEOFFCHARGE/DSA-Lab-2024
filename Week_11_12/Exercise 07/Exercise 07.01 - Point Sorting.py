"""Exercise 07.01 - Point Sorting"""
def pointSorting(value):
    return value[0] + value[1]

def bubbleSort(list, last):
    current = 0
    sorted = False
    while current <= last and not sorted:
        walker = last
        sorted = True
        while walker > current:
            if pointSorting(list[walker]) < pointSorting(list[walker - 1]) or \
                (pointSorting(list[walker]) == pointSorting(list[walker - 1]) and \
                list[walker][1] > list[walker - 1][1]):
                sorted = False
                list[walker], list[walker - 1] = list[walker - 1], list[walker]
            walker -= 1
        current += 1
    return list

def main():
    for _ in range(int(input())):
        temping = []
        for _ in range(int(input())):
            temping.append(tuple(map(int, input().split())))
        for i in bubbleSort(temping, len(temping) - 1):
            print(i[0], i[1])
main()
