# sum_root_to_leaf.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum = current_sum * 10 + node.val
            if not node.left and not node.right:
                return current_sum
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)

# ---------- TEST CASE ----------
if __name__ == "__main__":
    # Build tree: [1, 2, 3]
    #       1
    #      / \
    #     2   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    sol = Solution()
    result = sol.sumNumbers(root)
    print("Sum of all root-to-leaf numbers:", result)  # Output: 25
