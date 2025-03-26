"""Exercise 03.02 - Taking Turns"""
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

    def delete_first(self):
        temp = self.head.data
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
        self.count -= 1
        return temp

    def delete_last(self):
        parents_node = None
        current_node = self.head
        while current_node.next:
            parents_node = current_node
            current_node = current_node.next
        temp = current_node.data
        if parents_node:
            parents_node.next = None
        self.count -= 1
        return temp

    def traverse(self):
        position = True
        converse = True
        while self.count:
            if position and converse:
                print(self.delete_last(), end="")
                converse = False
            elif position:
                print(self.delete_first(), end="")
                position = False
                converse = True
            elif not position and converse:
                print(self.delete_first(), end="")
                converse = False
            elif not position:
                print(self.delete_last(), end="")
                position = True
                converse = True
            if self.count:
                print(" -> ", end="")
        print()

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()
main()
