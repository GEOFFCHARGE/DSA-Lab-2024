"""Exercise 01.04 - Laew Tae App V.2"""
class แล้วแต่แอพ:

    def __init__(self):
        self.food_list = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]
        self.ran_count = 0

    def random_foods(self):
        self.ran_count += 1

    def list_foods(self):
        print(sorted(self.food_list))

    def add_food_item(self, food):
        self.food_list.append(food)

def main():
    food = แล้วแต่แอพ()
    for _ in range(int(input())):
        food.add_food_item(input())
    food.list_foods()
main()
