from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    """Builds a binary tree from a level-order list."""
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while i < len(nodes):
        current = queue.popleft()

        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root

def zigzagLevelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

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

        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right

    return result

# ---------------- Run it ----------------

# User input like: 3 9 20 None None 15 7
input_nodes = input("Enter tree nodes (space-separated, use None for null): ")
node_list = [int(x) if x != 'None' else None for x in input_nodes.strip().split()]

tree_root = build_tree(node_list)

print("Input: root =", node_list)
print("Output:", zigzagLevelOrder(tree_root))
