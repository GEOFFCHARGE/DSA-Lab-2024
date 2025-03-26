"""Labs 05.03 - isIntersect(A, B, C)"""
def isIntersect(a, b, c):
    if a & b & c:
        return True
    return False

import json
def main():
    a = json.loads(input())
    b = json.loads(input())
    c = json.loads(input())
    a = {i for i in a}
    b = {i for i in b}
    c = {i for i in c}
    print(isIntersect(a, b, c))
main()
