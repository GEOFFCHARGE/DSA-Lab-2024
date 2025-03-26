"""[Mock Midterm] Music Box ( 14 คะแนน )"""
class DataNode:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class Song:

    def __init__(self, name, genre, durations):
        self.name = name
        self.genre = genre
        self.durations = int(durations)

    def show_info(self):
         return f"{self.name} <|> {self.genre} <|> {self.durations // 60}.{self.durations % 60:02d}"

class Queue:

    def __init__(self):
        self.head = None

    def enqueue(self, item):
        new_node = DataNode(item)
        if self.isEmpty():
            self.head = new_node
            return None
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def dequeue(self):
        if self.isEmpty():
            print("Underflow! Dequeue from an empty queue")
            return None
        current_node = self.head
        self.head = self.head.next
        return current_node.data

    def peek(self):
        if self.isEmpty():
            print("Underflow! peek from an empty queue")
            return None
        return self.head.data

    def isEmpty(self):
        return not self.head

    def show_Queue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return None
        numbers_node = 1
        current_node = self.head
        while current_node:
            print(f"Queue#{numbers_node} {current_node.data.show_info()}")
            numbers_node += 1
            current_node = current_node.next

    def lastSong(self, time):
        if self.isEmpty():
            print("There is no song in this queue!")
            return None
        summary_time = 0
        lastest_time = 0
        current_node = self.head
        while current_node:
            summary_time += current_node.data.durations
            current_node = current_node.next
        if time > summary_time:
            lastest_time = time % summary_time
        else:
            lastest_time = time
        summary_time = 0
        numbers_node = 1
        current_node = self.head
        while current_node:
            summary_time += current_node.data.durations
            if summary_time >= lastest_time:
                print(f"Queue#{numbers_node} {current_node.data.show_info()}")
                return None
            numbers_node += 1
            current_node = current_node.next

    def removeSong(self, name):
        if self.isEmpty():
            print(f"Can not Delete! {name} is not exist")
            return None
        if self.head.data.name == name:
            self.head = self.head.next
            return None
        parents_node = None
        current_node = self.head
        while current_node and current_node.data.name != name:
            parents_node = current_node
            current_node = current_node.next
        if not current_node:
            print(f"Can not Delete! {name} is not exist")
            return None
        parents_node.next = current_node.next

    def groupSong(self):
        if self.isEmpty():
            print("Nothing here! Please add some song")
            return None
        jpop, kpop, rndb = "", "", ""
        current_node = self.head
        while current_node:
            current_node_genre = current_node.data.genre
            current_node_names = current_node.data.name
            if current_node_genre == "JPOP" and not jpop:
                jpop += current_node_names
            elif current_node_genre == "JPOP":
                jpop += f" | {current_node_names}"
            elif current_node_genre == "KPOP" and not kpop:
                kpop += current_node_names
            elif current_node_genre == "KPOP":
                kpop += f" | {current_node_names}"
            elif current_node_genre == "R&B" and not rndb:
                rndb += current_node_names
            elif current_node_genre == "R&B":
                rndb += f" | {current_node_names}"
            current_node = current_node.next
        print(f"JPOP: {jpop}\nKPOP: {kpop}\nR&B: {rndb}")

    def undo(self):
        ...

    def rev_queue(self):
        ...


def main():
    q = Queue()
    while (choice := input()) != "End":
        current_node_genre, data = choice.split(": ")
        match current_node_genre:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    print("Dequeue item:", temp.show_info())
            case "peek":
                temp= q.peek()
                if temp:
                    print("Peek item:", temp.show_info())
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            case "rev":
                q.rev_queue()
    q.show_Queue()
main()
