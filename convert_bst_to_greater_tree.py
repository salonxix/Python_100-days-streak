class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.total_sum = 0

    def convertBST(self, root):
        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self.total_sum += node.val
            node.val = self.total_sum
            reverse_inorder(node.left)
        reverse_inorder(root)
        return root

# Helper to print the tree in level-order (for terminal display)
from collections import deque

def print_level_order(root):
    if not root:
        print("[]")
        return
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values for clean output
    while result and result[-1] is None:
        result.pop()
    print(result)

# Build sample tree: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
n0 = TreeNode(0)
n3 = TreeNode(3)
n2 = TreeNode(2, None, n3)
n1 = TreeNode(1, n0, n2)
n5 = TreeNode(5)
n8 = TreeNode(8)
n7 = TreeNode(7, None, n8)
n6 = TreeNode(6, n5, n7)
root = TreeNode(4, n1, n6)

# Convert and print
sol = Solution()
new_root = sol.convertBST(root)
print_level_order(new_root)
