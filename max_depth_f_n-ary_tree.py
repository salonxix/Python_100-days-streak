# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        if not root.children:
            return 1

        max_child_depth = 0
        for child in root.children:
            child_depth = self.maxDepth(child)
            max_child_depth = max(max_child_depth, child_depth)

        return max_child_depth + 1

# Tree construction for example: [1,null,3,2,4,null,5,6]
root = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])

# Create solution instance and compute depth
sol = Solution()
print(sol.maxDepth(root))
