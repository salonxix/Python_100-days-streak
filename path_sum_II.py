from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, path, current_sum):
            if not node:
                return

            path.append(node.val)
            current_sum += node.val

            # Check if it's a leaf and the path sum is correct
            if not node.left and not node.right and current_sum == targetSum:
                result.append(list(path))  # Copy current path

            dfs(node.left, path, current_sum)
            dfs(node.right, path, current_sum)

            path.pop()  # Backtrack

        dfs(root, [], 0)
        return result

# Build the tree: [5,4,8,11,null,13,4,7,2,null,null,5,1]
def build_tree():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    return root

if __name__ == "__main__":
    tree_root = build_tree()
    target = 22
    sol = Solution()
    paths = sol.pathSum(tree_root, target)
    print("Paths that sum to", target, "are:", paths)
