from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageOfLevels(root):
    if not root:
        return []

    result = []
    queue = deque([root])  # Queue for BFS

    while queue:
        level_sum = 0
        level_count = len(queue)

        for _ in range(level_count):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_count)  # Average for this level

    return result


# Example Usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(averageOfLevels(root))  # Output: [3.0, 14.5, 11.0]
