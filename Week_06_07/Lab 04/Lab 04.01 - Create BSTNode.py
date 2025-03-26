"""Lab 04.01 - Create BSTNode"""
class BSTNode:

    def __init__(self, data: int = None):
        self.data = data
        self.left = None
        self.right = None

def main():
    bst = BSTNode(input())
    print(bst.data)
    print(bst.left)
    print(bst.right)
main()
