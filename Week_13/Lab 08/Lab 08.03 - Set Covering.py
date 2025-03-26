"""Labs 08.03 - Set Covering"""
def sortIntersect(i):
    return len(i["Passed"])

import json
def main():
    results = []
    allCity = {i for i in json.loads(input())}
    station = [json.loads(input()) for _ in range(int(input()))]
    for i in station:
            i["Cities"] = {i for i in i["Cities"]}
    while True:
        for i in station:
            i["Passed"] = i["Cities"].intersection(allCity)
        station.sort(key=sortIntersect, reverse=True)
        if not station[0]["Passed"]:
            break
        allCity = {i for i in allCity if i not in station[0]["Passed"]}
        results.append(station[0]["Name"])
        station.pop(0)
    print(sorted(results))
main()
