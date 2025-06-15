from collections import deque

# Define the structure for a tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to check if a tree is height-balanced
def isBalanced(root):
    def check(node):
        if not node:
            return 0, True

        left_height, is_left_balanced = check(node.left)
        right_height, is_right_balanced = check(node.right)

        current_height = 1 + max(left_height, right_height)
        is_balanced = (
            is_left_balanced and 
            is_right_balanced and 
            abs(left_height - right_height) <= 1
        )
        return current_height, is_balanced

    _, balanced = check(root)
    return balanced

# Function to build a tree from a list (level order)
def buildTree(levels):
    if not levels or levels[0] is None:
        return None

    root = TreeNode(levels[0])
    queue = deque([root])
    i = 1

    while queue and i < len(levels):
        node = queue.popleft()
        
        # Left child
        if i < len(levels) and levels[i] is not None:
            node.left = TreeNode(levels[i])
            queue.append(node.left)
        i += 1

        # Right child
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

    # Build the tree
    root = buildTree(input_list)

    # Check if it is balanced
    result = isBalanced(root)

    # Print the result
    print("Is the binary tree balanced?:", result)
