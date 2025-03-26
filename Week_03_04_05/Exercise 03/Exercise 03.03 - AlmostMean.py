"""Exercise 03.03 - AlmostMean"""
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

    def almostmean(self, data):
        mean = data / self.count
        closest_idstd = None
        closest_score = 0
        current_node = self.head
        while current_node:
            idstd, score = current_node.data.split("\t")
            score = float(score)
            if mean >= score > closest_score:
                closest_idstd = idstd
                closest_score = score
            current_node = current_node.next
        return closest_idstd + "\t" + str(closest_score)

def main():
    mylist = SinglyLinkedList()
    totals = 0
    for _ in range(int(input())):
        status = input()
        mylist.insert_last(status)
        _, score = status.split("\t")
        totals += float(score)
    print(mylist.almostmean(totals))
main()
