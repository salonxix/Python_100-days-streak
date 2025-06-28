class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BST Iterator class
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        top_node = self.stack.pop()
        if top_node.right:
            self._leftmost_inorder(top_node.right)
        return top_node.val

    def hasNext(self):
        return len(self.stack) > 0

# Utility to build BST from level-order list input
from collections import deque

def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    q = deque([root])
    i = 1

    while i < len(nodes):
        curr = q.popleft()
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            q.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            q.append(curr.right)
        i += 1

    return root

# MAIN EXECUTION BASED ON EXAMPLE
commands = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
args = [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]

output = []

iterator = None

for command, arg in zip(commands, args):
    if command == "BSTIterator":
        root = build_tree(arg[0])
        iterator = BSTIterator(root)
        output.append(None)
    elif command == "next":
        output.append(iterator.next())
    elif command == "hasNext":
        output.append(iterator.hasNext())

print("Output:", output)
