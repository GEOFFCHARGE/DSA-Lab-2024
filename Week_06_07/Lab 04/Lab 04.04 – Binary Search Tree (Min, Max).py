"""Lab 04.04 - Binary Search Tree (Min, Max)"""
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

    def find_min(self):
        if not self.root:
            return None
        else:
            current_node = self.root
            while current_node.left:
                current_node = current_node.left
            return current_node.data

    def find_max(self):
        if not self.root:
            return None
        else:
            current_node = self.root
            while current_node.right:
                current_node = current_node.right
            return current_node.data

    def is_empty(self):
        return self.root == None

    def preorder(self, data: int = None):
        if data:
            print("->", data.data, end=" ")
            self.preorder(data.left)
            self.preorder(data.right)

    def inorder(self, data: int = None):
        if data:
            self.inorder(data.left)
            print("->", data.data, end=" ")
            self.inorder(data.right)

    def postorder(self, data: int = None):
        if data:
            self.postorder(data.left)
            self.postorder(data.right)
            print("->", data.data, end=" ")

    def traverse(self):
        if not self.is_empty():
            print("Preorder:", end=" ")
            self.preorder(self.root)
            print()
            print("Inorder:", end=" ")
            self.inorder(self.root)
            print()
            print("Postorder:", end=" ")
            self.postorder(self.root)
            print()
        else:
            print("This is an empty binary search tree.")

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())
main()
