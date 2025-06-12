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

def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# ---------------- Run it ----------------

# Accept user input: 1 2 3
input_p = input("Enter nodes for Tree p (space-separated, use None for null): ")
input_q = input("Enter nodes for Tree q (space-separated, use None for null): ")

list_p = [int(x) if x != 'None' else None for x in input_p.strip().split()]
list_q = [int(x) if x != 'None' else None for x in input_q.strip().split()]

tree_p = build_tree(list_p)
tree_q = build_tree(list_q)

print("Input:  p =", list_p, ", q =", list_q)
print("Output:", isSameTree(tree_p, tree_q))
