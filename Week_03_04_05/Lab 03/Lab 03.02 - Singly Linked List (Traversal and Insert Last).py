"""Lab 03.02 - Singly Linked List (Traversal and Insert Last)"""
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
        mylist.insert_last(input())
    mylist.traverse()
main()
