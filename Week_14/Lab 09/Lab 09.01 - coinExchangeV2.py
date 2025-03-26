"""Lab 09.01 - coinExchangeV2"""
def convertKey(data):
    return {int(k): int(v) for k, v in data.items()}

def sortMoneys(data):
    return data[0]

import json, math
def coinExchangeV2():
    amount = int(input())
    moneys = {k: v for k, v in sorted(convertKey(json.loads(input())).items(), key=sortMoneys, reverse=True)}
    gridDP = [{"coin": math.inf, "used": {k: 0 for k in moneys.keys()}} for _ in range(amount + 1)]
    gridDP[0]["coin"] = 0
    for i in moneys.keys():
        for j in range(amount + 1):
            if i <= j and gridDP[j - i]["coin"] + 1 < gridDP[j]["coin"] and gridDP[j - i]["used"][i] < moneys[i]:
                gridDP[j]["coin"] = gridDP[j - i]["coin"] + 1
                gridDP[j]["used"] = gridDP[j - i]["used"].copy()
                gridDP[j]["used"][i] += 1
    print(f"Amount: {amount}")
    if gridDP[amount]["coin"] == math.inf:
        print("Can not exchange.")
        return
    print("Coin exchange result:")
    for i in moneys.keys():
        print(f"  {i} baht = {gridDP[amount]["used"][i]} coins")
    print(f"Number of coins: {gridDP[amount]["coin"]}")
coinExchangeV2()
