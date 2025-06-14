class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    
    # Recursively build left and right subtree
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    
    return root

# Helper function to get level order traversal (for printing)
from collections import deque
def levelOrderTraversal(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val if node else None)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        if any(v is not None for v in level):  # Remove trailing None levels
            result.append(level)
    return result

# ------------------ Run ------------------

nums = [-10, -3, 0, 5, 9]
tree = sortedArrayToBST(nums)

print("Input: nums =", nums)
print("Output (Level Order):", levelOrderTraversal(tree))
