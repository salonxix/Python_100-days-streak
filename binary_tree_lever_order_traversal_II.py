from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderBottom(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result[::-1]  # Reverse for bottom-up order

# 🔧 Helper to build tree from level-order list
def buildTree(nodes):
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
        curr = queue.popleft()

        if nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1

    return root

# ------------------ Main ------------------

input_data = input("Enter tree level-order (comma separated, use 'null' for missing): ")
input_data = [int(x) if x != 'null' else None for x in input_data.strip().split(',')]
root = buildTree(input_data)

output = levelOrderBottom(root)
print("Bottom-up level order traversal:", output)
