# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: TreeNode):
        # Step 1: Find the height of the tree
        def get_height(node):
            if not node:
                return -1  # height of empty tree is -1
            return 1 + max(get_height(node.left), get_height(node.right))
        
        height = get_height(root)
        rows = height + 1
        cols = (2 ** (height + 1)) - 1  # total columns
        res = [["" for _ in range(cols)] for _ in range(rows)]
        
        # Step 2: Fill the matrix
        def fill(node, r, c, level):
            if not node:
                return
            res[r][c] = str(node.val)
            gap = 2 ** (height - r - 1)  # horizontal gap to children
            if node.left:
                fill(node.left, r + 1, c - gap, level + 1)
            if node.right:
                fill(node.right, r + 1, c + gap, level + 1)
        
        fill(root, 0, (cols - 1) // 2, 0)
        return res
