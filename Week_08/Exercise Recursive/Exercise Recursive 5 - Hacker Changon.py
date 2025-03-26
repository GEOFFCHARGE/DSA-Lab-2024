"""Exercise Recursive 5 - Hacker Changon"""
def HackerChangon(s, n, m):
    print(n)
    if n == m:
        return None
    return HackerChangon(s, n + s, m)

def main():
    s = 1
    n = int(input())
    m = int(input())
    if n > m:
        s = -s
    HackerChangon(s, n, m)
main()
