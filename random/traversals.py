from typing import List
from sorts import pseudo_random_gen
#practice with Preorder, Inorder and Postorder traversals
class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
def build_tree(root, index: int, arr):
    if index < len(arr):
        temp = Node(arr[index])
        root = temp

        root.left = build_tree(root, 2*index + 1, arr)
        root.right = build_tree(root, 2*index + 2, arr)
        return root
def inOrder(root, arr = []):
    if root:
        inOrder(root.left)
        arr.append(root.val)
        inOrder(root.right)
    return arr
def postOrder(root, arr = []):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        arr.append(root.val)
    return arr
def preOrder(root, arr = []):
    if root:
        arr.append(root.val)
        preOrder(root.left)
        preOrder(root.right)
    return arr

root = Node(0)
arr = [5, 3, 10, 2, 4, 8, 12]
"""
          5
         /  \
        3    10
       /  \  /  \
      2    4 8   12

"""
print("Array is {}".format(arr))
root = build_tree(root, 0, arr)
print("Preorder Traversal {}".format(str(preOrder(root))))
print("Inorder Traversal {}".format(str(inOrder(root))))
print("Postorder Traversal {}".format(str(postOrder(root))))


