# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        
        # If the node's value is less than low, we skip the left subtree
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # If the node's value is greater than high, we skip the right subtree
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # Otherwise, we recursively trim both subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
