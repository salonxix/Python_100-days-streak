from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    idx_map = {val: idx for idx, val in enumerate(inorder)}
    post_idx = [len(postorder) - 1]  # Use list to make it mutable in recursion

    def helper(in_left, in_right):
        if in_left > in_right:
            return None

        root_val = postorder[post_idx[0]]
        root = TreeNode(root_val)
        index = idx_map[root_val]

        post_idx[0] -= 1

        # Build right subtree first
        root.right = helper(index + 1, in_right)
        root.left = helper(in_left, index - 1)

        return root

    return helper(0, len(inorder) - 1)

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

    while result and result[-1] is None:
        result.pop()

    return result

# ------------------ Main ------------------

inorder_input = input("Enter inorder (comma separated): ")
postorder_input = input("Enter postorder (comma separated): ")

inorder = list(map(int, inorder_input.strip().split(',')))
postorder = list(map(int, postorder_input.strip().split(',')))

root = buildTree(inorder, postorder)
print("Level-order output:", printLevelOrder(root))
