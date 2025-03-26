"""Labs 08.01 - Coin Exchange"""
def convert_key(data):
    return {int(k): v for k, v in data.items()}

import json
def main():
    result = {}
    amount = int(input())
    remain = amount
    moneys = convert_key(json.loads(input()))
    for i, j in moneys.items():
        counts = min(remain // i, j)
        result[i] = counts
        remain -= counts * i
    print(f"Amount: {amount}")
    if not remain:
        coins = 0
        print("Coin exchange result:")
        for i, j in result.items():
            print(f"  {i} baht = {j} coins")
            coins += j
        print(f"Number of coins: {coins}")
    else:
        print("Coins are not enough.")
main()
