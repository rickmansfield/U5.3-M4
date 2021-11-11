"""
NOTE NOTE NOTE
The solutin starts on line 39
the code before it makes it work in VSCode
"""
class traverseTree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# r = traverseTree(5)
# r.left = traverseTree(12)
# r.right = traverseTree(32)
# r.right.left = traverseTree(8)
# r.right.right = traverseTree(4)

# r = traverseTree(5)
# r.left = traverseTree(10)
# r.right = traverseTree(25)
# r.right.left = traverseTree(12)
# r.right.right = traverseTree(3)

# r = traverseTree(5)
# r.left = traverseTree(6)
# r.right = traverseTree(6)
# r.left.left = traverseTree(7)
# r.left.right = traverseTree(7)
# r.left.left.left = traverseTree(8)
# r.left.left.right = traverseTree(8)

r = traverseTree(5)
r.left = traverseTree(7)
r.right = traverseTree(22)
r.right.left = traverseTree(17)
r.right.right = traverseTree(9)
def traverseTree(t):
    pass

print(traverseTree(r))