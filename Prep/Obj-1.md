# Unit 5.3 M4 

## Objective 1
-  Recall the different traversal types for a binary tree and implement a function to complete the traversal for each type

### Traversing Trees

[Canvas Link](https://lambdaschool.instructure.com/courses/1748/pages/objective-01-recall-the-different-traversal-types-for-a-binary-tree-and-implement-a-function-to-complete-the-traversal-for-each-type?module_item_id=622103)

- Depth-First
   - Preorder
      1. Visit the node (do something | print)
      2. Go to the left subtree
      3. Go to the right subtree
   - Inorder (ascending 1, 2, 3...)
      1. Go to the left subtree
      2. Visit node (do something | print)
      3. Go to the right subtree
    - Postorder
      1. Go to the left subtree
      2. Go to the right subtree
      3. Visit node (do something | print)
   
- Breadth-First (A.k.A Level Traversal)

The big difference between the two is the use of FIFO queues q.pop(0)  and LIFO stacks s.pop()