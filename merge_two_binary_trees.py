# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # Base cases
        if not root1:
            return root2
        if not root2:
            return root1
        
        # Merge current nodes
        merged = TreeNode(root1.val + root2.val)
        
        # Merge left children
        merged.left = self.mergeTrees(root1.left, root2.left)
        # Merge right children
        merged.right = self.mergeTrees(root1.right, root2.right)
        
        return merged

# Example usage:
# Tree 1: [1,3,2,5]
root1 = TreeNode(1)
root1.left = TreeNode(3, TreeNode(5))
root1.right = TreeNode(2)

# Tree 2: [2,1,3,None,4,None,7]
root2 = TreeNode(2)
root2.left = TreeNode(1, None, TreeNode(4))
root2.right = TreeNode(3, None, TreeNode(7))

sol = Solution()
merged_root = sol.mergeTrees(root1, root2)

# Function to print tree in level order for checking
from collections import deque
def level_order(root):
    if not root:
        return []
    result, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            result.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            result.append(None)
    return result

print(level_order(merged_root))  # Output: [3, 4, 5, 5, 4, None, 7]
