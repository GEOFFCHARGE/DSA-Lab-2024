"""Exercise 03.05 - Linked List (Insert Index)"""
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

    def insert_before(self, node, data):
        position = 1
        current_node = self.head
        while current_node.next and position != node:
            current_node = current_node.next
            position += 1
        new_node = DataNode(data)
        new_node.next = current_node.next
        current_node.next = new_node
        self.count += 1

    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    posit = int(input())
    value = input()
    if posit == mylist.count - 1:
        mylist.insert_last(value)
    elif not posit:
        mylist.insert_front(value)
    else:
        mylist.insert_before(posit, value)
    mylist.traverse()
main()
