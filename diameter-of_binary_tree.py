class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root):
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)

        height(root)
        return self.max_diameter

# Helper to build tree from level-order list
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    i = 0
    for j in range(1, len(values), 2):
        if nodes[i]:
            nodes[i].left = nodes[j]
            if j+1 < len(values):
                nodes[i].right = nodes[j+1]
        i += 1
        while i < len(nodes) and not nodes[i]:
            i += 1
    return nodes[0]

# Example Input
tree_vals = [1, 2, 3, 4, 5]  # Change this list to test other cases
root = build_tree(tree_vals)

# Solve and print
sol = Solution()
print("Diameter of the Tree:", sol.diameterOfBinaryTree(root))
