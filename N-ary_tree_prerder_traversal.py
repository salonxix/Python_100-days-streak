# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def preorder(self, root: 'Node') -> list:
        result = []

        def dfs(node):
            if not node:
                return
            result.append(node.val)
            for child in node.children:
                dfs(child)

        dfs(root)
        return result



root = Node(1, [
    Node(3, [Node(5), Node(6)]),
    Node(2),
    Node(4)
])

sol = Solution()
print(sol.preorder(root))
