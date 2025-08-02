from typing import Optional
from collections import defaultdict

# Tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = prefix[curr_sum - targetSum]

            prefix[curr_sum] += 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix[curr_sum] -= 1  # backtrack

            return count

        prefix = defaultdict(int)
        prefix[0] = 1
        return dfs(root, 0)

# Helper to build tree from list (level order)
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        curr = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
    return root

# Test 1
root1 = build_tree([10,5,-3,3,2,None,11,3,-2,None,1])
targetSum1 = 8
sol = Solution()
print("Output for Example 1:", sol.pathSum(root1, targetSum1))

# Test 2
root2 = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
targetSum2 = 22
print("Output for Example 2:", sol.pathSum(root2, targetSum2))
