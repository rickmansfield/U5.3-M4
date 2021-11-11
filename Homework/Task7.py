"""
NOTE NOTE NOTE
The solutin starts on line 39
the code before it makes it work in VSCode
"""
class binaryTreeInOrderTraversal:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# r = binaryTreeInOrderTraversal(5)
# r.left = binaryTreeInOrderTraversal(12)
# r.right = binaryTreeInOrderTraversal(32)
# r.right.left = binaryTreeInOrderTraversal(8)
# r.right.right = binaryTreeInOrderTraversal(4)

# r = binaryTreeInOrderTraversal(5)
# r.left = binaryTreeInOrderTraversal(10)
# r.right = binaryTreeInOrderTraversal(25)
# r.right.left = binaryTreeInOrderTraversal(12)
# r.right.right = binaryTreeInOrderTraversal(3)

# r = binaryTreeInOrderTraversal(5)
# r.left = binaryTreeInOrderTraversal(6)
# r.right = binaryTreeInOrderTraversal(6)
# r.left.left = binaryTreeInOrderTraversal(7)
# r.left.right = binaryTreeInOrderTraversal(7)
# r.left.left.left = binaryTreeInOrderTraversal(8)
# r.left.left.right = binaryTreeInOrderTraversal(8)

r = binaryTreeInOrderTraversal(5)
r.left = binaryTreeInOrderTraversal(7)
r.right = binaryTreeInOrderTraversal(22)
r.right.left = binaryTreeInOrderTraversal(17)
r.right.right = binaryTreeInOrderTraversal(9)

def binaryTreeInOrderTraversal(root):
    pass
    

print(binaryTreeInOrderTraversal(r))