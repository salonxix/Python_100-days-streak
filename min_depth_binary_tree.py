from collections import deque

# TreeNode definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to calculate minimum depth
def minDepth(root):
    if not root:
        return 0

    queue = deque([(root, 1)])  # node, depth

    while queue:
        node, depth = queue.popleft()

        # Check if it's a leaf node
        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

# Helper: Build tree from list (level-order)
def buildTree(levels):
    if not levels or levels[0] is None:
        return None

    root = TreeNode(levels[0])
    queue = deque([root])
    i = 1

    while queue and i < len(levels):
        node = queue.popleft()

        if i < len(levels) and levels[i] is not None:
            node.left = TreeNode(levels[i])
            queue.append(node.left)
        i += 1

        if i < len(levels) and levels[i] is not None:
            node.right = TreeNode(levels[i])
            queue.append(node.right)
        i += 1

    return root

# -------------------------------
# MAIN EXECUTION BLOCK
# -------------------------------
if __name__ == "__main__":
    # Example input
    input_list = [3, 9, 20, None, None, 15, 7]

    # Build binary tree
    root = buildTree(input_list)

    # Get minimum depth
    result = minDepth(root)

    # Output
    print("Minimum depth of the binary tree is:", result)
