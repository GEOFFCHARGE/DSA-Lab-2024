"""Exercise 03.01 - Indexing"""
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

    def traverse(self, posit):
        if not self.head:
            return "Error"
        current_node = self.head
        status1 = 0
        status2 = -(self.count)
        while current_node:
            if posit > 0 and status1 == posit:
                return current_node.data
            if posit < 0 and status2 == posit:
                return current_node.data
            current_node = current_node.next
            status1 += 1
            status2 += 1
        return "Error"

def main():
    mylist = SinglyLinkedList()
    while True:
        text = input()
        if text == "Last":
            break
        mylist.insert_last(text)
    posit = int(input())
    print(mylist.traverse(posit))
main()
