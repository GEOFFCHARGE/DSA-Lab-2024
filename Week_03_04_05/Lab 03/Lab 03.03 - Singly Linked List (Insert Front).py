"""Lab 03.03 - Singly Linked List (Insert Front)"""
class DataNode:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.count = 0
        self.head = None

    def insert_last(self, data):
        new_node = DataNode(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
        self.count += 1

    def insert_front(self, data):
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def traverse(self):
        if not self.head:
            print("This is an empty list.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end="")
            current_node = current_node.next
            if current_node:
                print(" -> ", end="")
        print()

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()
