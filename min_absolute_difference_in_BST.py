class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getMinimumDifference(root):
    prev = [None]
    min_diff = [float('inf')]

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        if prev[0] is not None:
            min_diff[0] = min(min_diff[0], abs(node.val - prev[0]))
        prev[0] = node.val
        inorder(node.right)

    inorder(root)
    return min_diff[0]

# Example Usage:
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)

print(getMinimumDifference(root1))  # Output: 1

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(48)
root2.right.left = TreeNode(12)
root2.right.right = TreeNode(49)

print(getMinimumDifference(root2))  # Output: 1
