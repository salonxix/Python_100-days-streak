class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:  # It's a leaf
        return root.val == targetSum
    # Recurse on children with updated sum
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)

def buildTree(levels):
    if not levels:
        return None
    nodes = [None if val is None else TreeNode(val) for val in levels]
    for i in range(len(nodes)):
        if nodes[i]:
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(nodes):
                nodes[i].left = nodes[left]
            if right < len(nodes):
                nodes[i].right = nodes[right]
    return nodes[0]

# 🌳 Input Tree
root = buildTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
targetSum = 22

# ✅ Output like LeetCode
print(str(hasPathSum(root, targetSum)).lower())
