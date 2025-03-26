"""Exercise Recursive 3 - OneTwo"""
def onetwo(x, y, n):
    if n == 1:
        return x
    if n == 2:
        return y
    if n >= 3:
        s1 = x
        s2 = y
        s3 = s2 + s1
        n -= 1
        if not n:
            return s3
        return onetwo(s2, s3, n)

def main():
    print(onetwo("1", "2", int(input())))
main()
