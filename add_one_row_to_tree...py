# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        # Special case: adding at root
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        # Helper DFS
        def dfs(node, current_depth):
            if not node:
                return
            
            # If one level above target depth
            if current_depth == depth - 1:
                # Store original children
                old_left = node.left
                old_right = node.right
                
                # Create new nodes
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                
                # Attach old subtrees
                node.left.left = old_left
                node.right.right = old_right
            else:
                dfs(node.left, current_depth + 1)
                dfs(node.right, current_depth + 1)
        
        dfs(root, 1)
        return root

# Example usage:
# Tree: [4,2,6,3,1,5]
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(3), TreeNode(1))
root.right = TreeNode(6, TreeNode(5))

sol = Solution()
new_root = sol.addOneRow(root, 1, 2)

# Function to print level order for verification
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

print(level_order(new_root))  # Output: [4, 1, 1, 2, None, None, 6, 3, 1, 5]
