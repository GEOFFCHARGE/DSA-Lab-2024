"""Lab 04.06 - Binary Search Tree (Delete All Cases)"""
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

    def delete(self, data: int = None):
        parents_node = None
        current_node = self.root
        while current_node and current_node.data != data:
            if current_node.data > data:
                parents_node = current_node
                current_node = current_node.left
            else:
                parents_node = current_node
                current_node = current_node.right
        if not current_node:
            print("Delete Error,", data,"is not found in Binary Search Tree.")
            return None
        if not current_node.left and not current_node.right:
            if self.root == current_node:
                self.root = None
            elif parents_node.left == current_node:
                parents_node.left = None
            else:
                parents_node.right = None
        elif current_node.left and not current_node.right:
            if self.root == current_node:
                self.root = current_node.left
            elif parents_node.left == current_node:
                parents_node.left = current_node.left
            else:
                parents_node.right = current_node.left
        elif not current_node.left and current_node.right:
            if self.root == current_node:
                self.root = current_node.right
            elif parents_node.left == current_node:
                parents_node.left = current_node.right
            else:
                parents_node.right = current_node.right
        else:
            parents_node = current_node
            deleted_node = parents_node.left
            while deleted_node.right:
                parents_node = deleted_node
                deleted_node = deleted_node.right
            current_node.data = deleted_node.data
            if parents_node.left == deleted_node:
                parents_node.left = deleted_node.left
            else:
                parents_node.right = deleted_node.left

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
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()
main()
