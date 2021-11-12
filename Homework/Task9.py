"""
NOTE NOTE NOTE
The solutin starts on line 39
the code before it makes it work in VSCode
"""
class treePaths:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# r = treePaths(5)
# r.left = treePaths(12)
# r.right = treePaths(32)
# r.right.left = treePaths(8)
# r.right.right = treePaths(4)

# r = treePaths(5)
# r.left = treePaths(10)
# r.right = treePaths(25)
# r.right.left = treePaths(12)
# r.right.right = treePaths(3)

# r = treePaths(5)
# r.left = treePaths(6)
# r.right = treePaths(6)
# r.left.left = treePaths(7)
# r.left.right = treePaths(7)
# r.left.left.left = treePaths(8)
# r.left.left.right = treePaths(8)

# r = treePaths(5)
# r.left = treePaths(7)
# r.right = treePaths(22)
# r.right.left = treePaths(17)
# r.right.right = treePaths(9)
# def treePaths(t):
#     pass

def treePaths(root, path = None, result = None):
    if result is None:
        result = []
    
    if path is None:
        path = []
        
    if root is None:
        return path
        
    path.append(f"{root.value}")
    
    if root.left is None and root.right is None:
        result.append("->".join(path))
    
    treePaths(root.left, path, result)
    treePaths(root.right, path, result)

    path.pop()
    return result

# print(treePaths(r))