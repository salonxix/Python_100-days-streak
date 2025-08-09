# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k):
    seen = set()  # Stores values we've seen

    def dfs(node):
        if not node:
            return False

        # If complement exists in set, we found a pair
        if (k - node.val) in seen:
            return True

        seen.add(node.val)

        # Continue searching in left and right subtrees
        return dfs(node.left) or dfs(node.right)

    return dfs(root)


# Example Usage
root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2), TreeNode(4))
root.right = TreeNode(6, None, TreeNode(7))

print(findTarget(root, 9))   # Output: True
print(findTarget(root, 28))  # Output: False
