class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def build_tree(nodes):
    """Build binary tree from level order list."""
    if not nodes or nodes[0] is None:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    
    while i < len(nodes):
        node = queue.popleft()
        
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1

    return root

def maxDepth(root):
    if not root:
        return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return 1 + max(left, right)

# ---------------- Run it ----------------

# Example: 3 9 20 None None 15 7
input_nodes = input("Enter tree nodes (space-separated, use None for null): ")
node_list = [int(x) if x != 'None' else None for x in input_nodes.strip().split()]

tree_root = build_tree(node_list)

print("Input: root =", node_list)
print("Output:", maxDepth(tree_root))
