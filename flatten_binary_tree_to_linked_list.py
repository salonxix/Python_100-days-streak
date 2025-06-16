from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)

        # Store left and right subtrees
        left_subtree = root.left
        right_subtree = root.right

        # Move left subtree to the right
        root.left = None
        root.right = left_subtree

        # Move to the end of new right subtree
        current = root
        while current.right:
            current = current.right

        # Attach original right subtree
        current.right = right_subtree

# Build the tree: [1,2,5,3,4,null,6]
def build_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    return root

# Helper to print flattened tree
def print_flattened_tree(root: TreeNode):
    while root:
        print(root.val, end=" -> ")
        root = root.right
    print("None")

if __name__ == "__main__":
    tree_root = build_tree()
    sol = Solution()
    sol.flatten(tree_root)
    print("Flattened tree (pre-order linked list):")
    print_flattened_tree(tree_root)
