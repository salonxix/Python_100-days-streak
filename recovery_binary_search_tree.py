class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    """Build tree from level order list"""
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

def tree_to_list(root):
    """Convert tree to level order list for display"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Trim trailing None
    while result and result[-1] is None:
        result.pop()

    return result

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

class Solution:
    def recoverTree(self, root):
        self.first = self.second = self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)

        inorder(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val

# ---------------- Run it ----------------

# Accept user input: 1 3 None None 2
input_str = input("Enter BST nodes in level-order (space-separated, use None for nulls): ")
node_list = [int(x) if x != 'None' else None for x in input_str.strip().split()]

# Build Tree
root = build_tree(node_list)
print("Input:  root =", tree_to_list(root))

# Recover Tree
Solution().recoverTree(root)

# Show Output
print("Output:", tree_to_list(root))
