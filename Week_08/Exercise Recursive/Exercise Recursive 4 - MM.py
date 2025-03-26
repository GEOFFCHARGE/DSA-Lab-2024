"""Exercise Recursive 4 - MM"""
def MM(mx, mn):
    n = input()
    if n == "End":
        return f"Max: {mx}\nMin: {mn}"
    n = int(n)
    if n > mx:
        mx = n
    if n < mn:
        mn = n
    return MM(mx, mn)

def main():
    print(MM(-1, 999))
main()
