"""Lab 04.02 - Binary Search Tree (Preorder, Insert)"""
class BSTNode:

    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, data: int = None):
        new_node = BSTNode(data)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if current_node.data > new_node.data:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = new_node
                        break
                else:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = new_node
                        break

    def preorder(self, data: int = None):
        if data:
            print("->", data.data, end=" ")
            self.preorder(data.left)
            self.preorder(data.right)

def main():
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    print("Preorder: ", end="")
    my_bst.preorder(my_bst.root)
main()
