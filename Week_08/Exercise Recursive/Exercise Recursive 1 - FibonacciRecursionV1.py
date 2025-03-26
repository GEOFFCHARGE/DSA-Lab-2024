"""Exercise Recursive 1 - FibonacciRecursionV1"""
def fibo(n):
    if n > 1:
        return fibo(n - 1) + fibo(n - 2)
    return n

def main():
    print(fibo(int(input())))
main()
