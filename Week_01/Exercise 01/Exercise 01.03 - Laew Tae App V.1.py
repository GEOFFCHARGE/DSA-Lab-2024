"""Exercise 01.03 - Laew Tae App V.1"""
class แล้วแต่แอพ:

    def __init__(self):
        self.food_list = ["Pizza", "Fried Chicken", "Hamburger", "Steak"]
        self.ran_count = 0

    def random_foods(self):
        self.ran_count += 1

    def list_foods(self):
        print(sorted(self.food_list))

def main():
    x = แล้วแต่แอพ()
    x.list_foods()
main()
