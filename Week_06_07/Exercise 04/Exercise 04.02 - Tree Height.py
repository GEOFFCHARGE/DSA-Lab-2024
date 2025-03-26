"""Exercise 04.02 - Tree Height"""
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

    def height(self, data):
        if not data:
            return 0
        left_height = self.height(data.left)
        right_height = self.height(data.right)
        return max(left_height, right_height) + 1

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
    print(my_bst.height(my_bst.root))
main()
