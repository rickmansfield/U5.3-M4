"""
NOTE NOTE NOTE
The solutin starts on line 39
the code before it makes it work in VSCode
"""
class traverseTree:
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

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

# r = traverseTree(5)
# r.left = traverseTree(7)
# r.right = traverseTree(22)
# r.right.left = traverseTree(17)
# r.right.right = traverseTree(9)

r = traverseTree(1)
r.left = traverseTree(2)
r.left.right = traverseTree(3)
r.right = traverseTree(4)
r.right.left = traverseTree(5)

def traverseTree(t):
    q = []
    results = []
    q.append(t)

    while len(q) > 0:
        cur = q.pop(0)
        if cur is None:
            continue
        results.append(cur.value)
        
        if cur.left:
            q.append(cur.left)
            
        if cur.right:
            q.append(cur.right)
    return results 
    

print(traverseTree(r))