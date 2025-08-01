# Day 72: Sum of Left Leaves in a Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    if not root:
        return 0

    total = 0
    if root.left and not root.left.left and not root.left.right:
        total += root.left.val

    total += sumOfLeftLeaves(root.left)
    total += sumOfLeftLeaves(root.right)
    return total

# Helper function to build tree from level-order input
def build_tree(values):
    if not values or values[0] == 'null':
        return None

    nodes = [None if val == 'null' else TreeNode(int(val)) for val in values]
    kid_index = 1
    for i in range(len(nodes)):
        if nodes[i]:
            if kid_index < len(nodes):
                nodes[i].left = nodes[kid_index]
                kid_index += 1
            if kid_index < len(nodes):
                nodes[i].right = nodes[kid_index]
                kid_index += 1
    return nodes[0]

# -------- Terminal Input and Execution --------

if __name__ == "__main__":
    input_str = input("Enter tree nodes in level order (comma separated, use 'null' for empty):\n")
    input_list = input_str.strip().split(',')
    root = build_tree(input_list)

    result = sumOfLeftLeaves(root)
    print("Sum of all left leaves:", result)
