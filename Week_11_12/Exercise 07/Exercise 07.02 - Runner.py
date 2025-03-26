"""Exercise 07.02 - Runner"""
def Runner(value):
    return value[2] / value[1]

def bubbleSort(list, last):
    walker = last
    while walker > 0:
        if Runner(list[walker]) < Runner(list[walker - 1]) or \
            (Runner(list[walker]) == Runner(list[walker - 1]) and \
            list[walker][1] > list[walker - 1][1]):
            list[walker], list[walker - 1] = list[walker - 1], list[walker]
        walker -= 1
    return list[0][0]

def main():
    temps = []
    phase = float(input())
    for i in range(1, int(input()) + 1):
        speed, start = map(int, input().split())
        temps.append((i, speed, phase - start))
    print(bubbleSort(temps, len(temps) - 1))
main()
