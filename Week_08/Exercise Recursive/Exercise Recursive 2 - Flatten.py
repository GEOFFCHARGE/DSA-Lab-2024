"""Exercise Recursive 2 - Flatten"""
def Flatten(list_raw):
    list_fix = []
    for i in list_raw:
        if isinstance(i, list):
            list_fix.extend(Flatten(i))
        else:
            list_fix.append(i)
    return sorted(list_fix, reverse=True)

import json
def main():
    print(Flatten(json.loads(input())))
main()
