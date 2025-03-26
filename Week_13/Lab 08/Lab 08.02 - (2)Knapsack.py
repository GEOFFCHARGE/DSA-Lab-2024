"""Labs 08.02 - (2)Knapsack"""
class Item:

    def __init__(self, name: str, price: int, weight: float, cost: float):
        self.name = name
        self.price = price
        self.weight = weight
        self.cost = cost

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight

    def get_cost(self):
        return self.cost

def sortValues(checks):
    return checks[0]

def knapsack(items, capacity):
    checks = []
    totals = 0
    weight = 0
    for i in items:
        checks.append((i.get_cost(), i))
    checks.sort(key=sortValues, reverse=True)
    print(f"Knapsack Size: {capacity} kg\n===============================")
    for _, j in checks:
        if weight + j.get_weight() <= capacity:
            print(f"{j.get_name()} -> {j.get_weight()} kg -> {j.get_price()} THB")
            totals += j.get_price()
            weight += j.get_weight()
    print(f"Total: {totals} THB")

import json
def main():
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in["name"], item_in["price"], item_in["weight"], item_in["price"] / item_in["weight"]))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()
