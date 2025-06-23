# binary_tree_preorder.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            result.append(node.val)  # Visit root
            dfs(node.left)           # Then left
            dfs(node.right)          # Then right

        dfs(root)
        return result

# 🔧 Helper to build tree from list input (for testing)
from collections import deque

def build_tree(level_order):
    if not level_order:
        return None
    root = TreeNode(level_order[0])
    queue = deque([root])
    i = 1
    while queue and i < len(level_order):
        node = queue.popleft()
        if level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1
    return root

# 🧪 Test
if __name__ == "__main__":
    # Example 1
    root = build_tree([1, None, 2, 3])
    sol = Solution()
    print("Output:", sol.preorderTraversal(root))  # Output: [1, 2, 3]
