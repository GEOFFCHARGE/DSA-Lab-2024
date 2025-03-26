"""Labs 05.01 - Summation (แบบที่ 1)"""
def sunmation(n):
    m = 0
    for i in range(1, n + 1):
        m += i
    return m

def main():
    print(sunmation(int(input())))
main()
