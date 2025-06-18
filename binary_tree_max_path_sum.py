# binary_tree_max_path_sum.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float('-inf')

        def max_gain(node):
            if not node:
                return 0
            
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            new_path = node.val + left_gain + right_gain
            self.maxSum = max(self.maxSum, new_path)

            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return self.maxSum

# ---------- DRIVER CODE TO TEST ------------
# Create the tree manually: [1, 2, 3]
#       1
#      / \
#     2   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

sol = Solution()
result = sol.maxPathSum(root)
print("Maximum Path Sum:", result)  # Output should be 6
