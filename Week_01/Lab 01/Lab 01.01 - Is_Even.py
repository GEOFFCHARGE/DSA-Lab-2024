"""Lab 01.01 - Is_Even"""
def is_even():
    n = input()
    if n[-1] in ("0", "2", "4", "6", "8"):
        print(True)
    else:
        print(False)
is_even()
