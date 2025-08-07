# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: 'Node') -> list:
        result = []

        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)
            result.append(node.val)

        dfs(root)
        return result

# Example usage: Tree = [1,null,3,2,4,null,5,6]
# Construct tree manually
#       1
#     / | \
#    3  2  4
#   / \
#  5   6

root = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])

sol = Solution()
print(sol.postorder(root))
