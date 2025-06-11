from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

# Function to build a binary tree from a level-order list
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()
        
        # Left child
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        
        # Right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root

# Inorder traversal (recursive)
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node: Optional[TreeNode]):
        if node:
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

    dfs(root)
    return result

# Example usage:
user_input = [1, None, 2, 3]  # Replace this list with your own input
root = build_tree(user_input)
output = inorderTraversal(root)
print("Inorder Traversal Output:", output)
