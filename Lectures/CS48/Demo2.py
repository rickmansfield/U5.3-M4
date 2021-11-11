"""
You are given the values from a preorder and an inorder tree traversal. Write a
function that can take those inputs and output a binary tree.
*Note: assume that there will not be any duplicates in the tree.*
Example:
Inputs:
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]
Output:
    5
   / \
  7  22
    /  \
   13   9

t = TreeNode(5)
t.left = TreeNode(7)
t.right = TreeNode(22)
t.right.left = TreeNode(13)
t.right.right = TreeNode(9)

helper function?
keep track of pre order index?
create a new node for the root of the tree using the first item in the pre order list as the value
keep track of the relationship between the values and thier index using a dictionary (populate the dict)
call the helper function with no args to start of a chain reaction of recursive calls in the helper function

--- Helper Function ---
take in an input of left, and an input of right such that the in_left defaults to zero and the in_right default to the len(inorder)
-- deal with a convergence of the inleft and inright (base case)

take the root value from the preorder list
create a new treenode using the root value
get the idx from the dict by passing the root value as a key.
do setup for recursive calls
do a recursive call to the helper function passing the in_left and the idx (for the left)
do a recursive call to the helper function passing the idx + 1 and the in_right (for the right)
- return the root node once all recursive calls resolve




"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder, inorder):
  def helper(in_left = 0, in_right = len(inorder)):
    nonlocal pre_idx
    if in_left == in_right:
      return None
    
    root_value = preorder[pre_idx]
    root = TreeNode(root_value)

    idx = idx_map[root_value]

    pre_idx += 1

    root.left = helper(in_left, idx)
    root.right = helper(idx + 1, in_right)
    return root

  pre_idx = 0
  idx_map = {}

  for idx, value in enumerate(inorder):
    idx_map[value] = idx

  return helper()

    


# test
preorder = [5,7,22,13,9]
inorder = [7,5,13,22,9]

t = build_tree(preorder, inorder)
print(t.val, t.left.val, t.right.val, t.right.left.val, t.right.right.val)