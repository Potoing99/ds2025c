import sys
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(node, key):  # BST
  if node is None:
    return TreeNode(key)
  else:
    if key < node.val:
      node.left = insert(node.left, key)
    else:
      node.right = insert(node.right, key)
  return node


def post_order(node):
  if node:
    post_order(node.left)  # left subtree
    post_order(node.right)  # right subtree
    print(node.val)  # process


inputs = [50, 30, 24, 5, 28, 45, 98, 52, 60]  # preorder input
root = None
# for i in sys.stdin:
for i in inputs:
  # root = insert(root, int(i.strip()))
  root = insert(root, i)

post_order(root)