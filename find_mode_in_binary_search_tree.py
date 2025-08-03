class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMode(root):
    from collections import defaultdict

    freq = defaultdict(int)
    max_count = 0

    def inorder(node):
        nonlocal max_count
        if not node:
            return
        inorder(node.left)
        freq[node.val] += 1
        max_count = max(max_count, freq[node.val])
        inorder(node.right)

    inorder(root)
    return [key for key, val in freq.items() if val == max_count]

# Example Usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
print(findMode(root))  # Output: [2]

root2 = TreeNode(0)
print(findMode(root2))  # Output: [0]
