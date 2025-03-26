"""Lab 09.02 - KnapsackV2"""
class Item:

    def __init__(self, name: str, price: int, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight

def sorting(i):
    return i.get_name()

import json
def main():
    knapItem = []
    knapsack = json.loads(input())
    numItems = len(knapsack)
    bagLimit = int(input())
    gridItem = [[{"item" : [], "cost" : 0} for _ in range(bagLimit)] for _ in range(numItems)]
    for i in knapsack:
        knapItem.append(Item(i[0], i[1], i[2]))
    for i, j in enumerate(knapItem):
        for k in range(bagLimit):
            if not i and j.get_weight() <= k + 1:
                gridItem[i][k]["item"].append(j)
                gridItem[i][k]["cost"] = j.get_price()
            elif j.get_weight() > k + 1:
                gridItem[i][k]["item"] = gridItem[i - 1][k]["item"]
                gridItem[i][k]["cost"] = gridItem[i - 1][k]["cost"]
            elif j.get_weight() == k + 1:
                if j.get_price() > gridItem[i - 1][k]["cost"]:
                    gridItem[i][k]["item"].append(j)
                    gridItem[i][k]["cost"] = j.get_price()
                else:
                    gridItem[i][k]["item"] = gridItem[i - 1][k]["item"]
                    gridItem[i][k]["cost"] = gridItem[i - 1][k]["cost"]
            elif j.get_weight() < k + 1:
                if j.get_price() + gridItem[i - 1][((k + 1) - j.get_weight()) - 1]["cost"] > gridItem[i - 1][k]["cost"]:
                    gridItem[i][k]["item"].extend(gridItem[i - 1][((k + 1) - j.get_weight()) - 1]["item"])
                    gridItem[i][k]["item"].append(j)
                    gridItem[i][k]["cost"] = j.get_price() + gridItem[i - 1][((k + 1) - j.get_weight()) - 1]["cost"]
                elif j.get_price() + gridItem[i - 1][((k + 1) - j.get_weight()) - 1]["cost"] == gridItem[i - 1][k]["cost"]:
                    if 1 + len(gridItem[i - 1][((k + 1) - j.get_weight()) - 1]["item"]) > len(gridItem[i - 1][k]["item"]):
                        gridItem[i][k]["item"].extend(gridItem[i - 1][((k + 1) - j.get_weight()) - 1]["item"])
                        gridItem[i][k]["item"].append(j)
                        gridItem[i][k]["cost"] = j.get_price() + gridItem[i - 1][((k + 1) - j.get_weight()) - 1]["cost"]
                else:
                    gridItem[i][k]["item"] = gridItem[i - 1][k]["item"]
                    gridItem[i][k]["cost"] = gridItem[i - 1][k]["cost"]
    print(f"Total: {gridItem[-1][-1]["cost"]}")
    for i in sorted(gridItem[-1][-1]["item"], key=sorting):
        print(f"{i.get_name()} -> {i.get_weight()} kg -> {i.get_price()} THB")
main()
