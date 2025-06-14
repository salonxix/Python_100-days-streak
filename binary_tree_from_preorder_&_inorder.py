from collections import deque

# Tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to build tree from preorder and inorder
def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)

    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])

    return root

# Function to print level order traversal as list (with 'None' for nulls)
def printLevelOrder(root):
    if not root:
        return []

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

    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()

    return result

# ------------------ Main ------------------

# User input
preorder_input = input("Enter preorder (comma separated): ")
inorder_input = input("Enter inorder (comma separated): ")

# Convert string input to lists of integers
preorder = list(map(int, preorder_input.strip().split(',')))
inorder = list(map(int, inorder_input.strip().split(',')))

# Build tree and print level-order
root = buildTree(preorder, inorder)
print("Level-order output:", printLevelOrder(root))
