class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    """Build binary tree from level-order list"""
    if not nodes or nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

def isMirror(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return (t1.val == t2.val and 
            isMirror(t1.left, t2.right) and 
            isMirror(t1.right, t2.left))

def isSymmetric(root):
    return isMirror(root, root)

# ---------------- Run it ----------------

# User input like: 1 2 2 3 4 4 3
input_nodes = input("Enter nodes (space-separated, use None for null): ")
node_list = [int(x) if x != 'None' else None for x in input_nodes.strip().split()]

tree_root = build_tree(node_list)

print("Input: root =", node_list)
print("Output:", isSymmetric(tree_root))
