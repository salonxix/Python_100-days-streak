class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    """Build binary tree from level-order list where None means no child."""
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min_val = root.val
        self.second_min = float('inf')

        def dfs(node):
            if not node:
                return
            if min_val < node.val < self.second_min:
                self.second_min = node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.second_min if self.second_min < float('inf') else -1

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    # Example input: 2 2 5 null null 5 7
    raw_input = input("Enter tree in level order (use 'null' for None): ").split()
    values = [int(x) if x != "null" else None for x in raw_input]

    root = build_tree(values)
    result = Solution().findSecondMinimumValue(root)
    print("Second Minimum Value:", result)
