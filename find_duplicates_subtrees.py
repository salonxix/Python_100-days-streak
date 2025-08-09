from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDuplicateSubtrees(root):
    seen = defaultdict(int)  # Maps serialization -> frequency
    duplicates = []

    def serialize(node):
        if not node:
            return "#"

        # Serialize subtree: "value,left_serial,right_serial"
        serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
        seen[serial] += 1

        # If we see this serialization exactly twice, it's a duplicate
        if seen[serial] == 2:
            duplicates.append(node)

        return serial

    serialize(root)
    return duplicates


# Example Usage
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4))
root.right = TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4))

result = findDuplicateSubtrees(root)
for node in result:
    print(node.val)  # Output could be: 2, 4
