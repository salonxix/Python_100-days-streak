# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        from collections import deque
        
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])  # (node, position_index)
        
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]
            _, last_index = queue[-1]
            # Calculate current level width
            max_width = max(max_width, last_index - first_index + 1)
            
            # Process the next level
            for _ in range(level_length):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return max_width
