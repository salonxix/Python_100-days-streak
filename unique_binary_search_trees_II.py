from typing import Optional, List
from collections import deque

# TreeNode definition
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

# Function to generate all unique BSTs
def generateTrees(n: int) -> List[Optional[TreeNode]]:
    if n == 0:
        return []

    def build(start: int, end: int) -> List[Optional[TreeNode]]:
        if start > end:
            return [None]
        all_trees = []
        for i in range(start, end + 1):
            left_subtrees = build(start, i - 1)
            right_subtrees = build(i + 1, end)

            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    all_trees.append(root)
        return all_trees

    return build(1, n)

# Helper to convert tree to list (level order)
def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

# -------- Main Flow --------
if __name__ == "__main__":
    n = int(input("Enter n (number of nodes): "))
    bst_roots = generateTrees(n)

    print(f"\nTotal Unique BSTs: {len(bst_roots)}")
    print("Output:")
    for i, tree in enumerate(bst_roots, 1):
        print(f"{i}: {tree_to_list(tree)}")
