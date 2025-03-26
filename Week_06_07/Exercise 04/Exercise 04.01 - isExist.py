"""Exercise 04.01 - isExist"""
class BSTNode:

    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, data: int = None):
        inserts_node = BSTNode(data)
        if not self.root:
            self.root = inserts_node
        else:
            current_node = self.root
            while True:
                if current_node.data > inserts_node.data:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = inserts_node
                        break
                else:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = inserts_node
                        break

    def isExist(self, data: int = None):
        current_node = self.root
        while current_node and current_node.data != data:
            if current_node.data > data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        if not current_node:
            return False
        return True

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
    print(my_bst.isExist(int(input())))
main()
