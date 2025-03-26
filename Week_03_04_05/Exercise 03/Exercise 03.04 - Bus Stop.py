"""Exercise 03.04 - Bus Stop"""
class DataNode:

    def __init__(self, station, peoples):
        self.station = station
        self.peoples = peoples
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def enqueue(self, station, peoples):
        new_node = DataNode(station, peoples)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def busStop(self, p, n):
        seats = ""
        getOn = 0
        getOf = 0
        for i in range(1, n + 1):
            current_node = self.head
            while current_node.station != i:
                current_node = current_node.next
            for j in seats.split():
                if i == int(j):
                    seats = seats.replace(" " + j + " ", "", 1)
                    getOn -= 1
                    getOf += 1
            for k in current_node.peoples:
                if i < int(k) and getOn < p:
                    seats += " " + k + " "
                    getOn += 1
        return getOf

def main():
    b = SinglyLinkedList()
    p = int(input())
    n = int(input())
    for _ in range(n):
        station = ""
        peoples = ""
        started = False
        informs = input()
        for i in informs:
            if i == " " and not started:
                started = True
            elif started:
                peoples += i
            else:
                station += i
        b.enqueue(int(station), peoples.split())
    print(b.busStop(p, n))
main()
