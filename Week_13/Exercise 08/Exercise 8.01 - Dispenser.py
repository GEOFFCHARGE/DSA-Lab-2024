"""Exercise 8.01 - Dispenser"""
def finding(colNumber):
    return colNumber[0][0], -len(colNumber[0]), colNumber

def main():
    maxValues = ""
    n = int(input())
    m = int(input())
    dispenser = [[] for _ in range(m)]
    for _ in range(n):
        for i, j in enumerate(input().split()):
            dispenser[i].append(j)
    dispenser = [i[::-1] for i in dispenser]
    while dispenser:
        dispenser.sort(key=finding, reverse=True)
        maxValues += dispenser[0].pop(0)
        dispenser = [i for i in dispenser if i]
    print(int(maxValues))
main()
