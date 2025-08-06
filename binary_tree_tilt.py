# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total_tilt = 0

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            node_tilt = abs(left_sum - right_sum)

            self.total_tilt += node_tilt

            return node.val + left_sum + right_sum

        dfs(root)
        return self.total_tilt

# Example usage:
# Tree: [4,2,9,3,5,null,7]
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(3), TreeNode(5))
root.right = TreeNode(9, None, TreeNode(7))

sol = Solution()
print(sol.findTilt(root))
