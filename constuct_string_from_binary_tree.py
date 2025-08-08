# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        # Helper function for recursion
        def preorder(node):
            if not node:
                return ""
            
            # Start with current node value
            result = str(node.val)
            
            # If there is a left child, add it
            if node.left:
                result += "(" + preorder(node.left) + ")"
            # If no left but right child exists, add empty parentheses
            elif node.right:
                result += "()"
            
            # If there is a right child, add it
            if node.right:
                result += "(" + preorder(node.right) + ")"
            
            return result
        
        return preorder(root)

# Example usage:
# Construct tree: [1,2,3,None,4]
root = TreeNode(1)
root.left = TreeNode(2, None, TreeNode(4))
root.right = TreeNode(3)

sol = Solution()
print(sol.tree2str(root))  # Output: "1(2()(4))(3)"
