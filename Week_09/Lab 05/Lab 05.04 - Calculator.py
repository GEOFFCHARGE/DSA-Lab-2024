"""Labs 05.04 - Calculator"""
def calculator(n):
    if n == 1:
        return 1
    m = n
    for i in range(1, n + 1):
        m += len(str(i))
    return m

def main():
    print(calculator(int(input())))
main()
