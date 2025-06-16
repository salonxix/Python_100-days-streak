class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: 'Node') -> 'Node':
    if not root:
        return None

    if root.left and root.right:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left

    connect(root.left)
    connect(root.right)

    return root

# Helper function to build perfect binary tree from list
def build_perfect_tree():
    nodes = [Node(i) for i in range(1, 8)]  # [1..7]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    return nodes[0]

# Function to serialize the next-pointers as shown in the output
def serialize_next_pointers(root):
    result = []
    level_start = root
    while level_start:
        curr = level_start
        while curr:
            result.append(curr.val)
            curr = curr.next
        result.append("#")
        level_start = level_start.left
    return result

# Main function
if __name__ == "__main__":
    root = build_perfect_tree()
    connect(root)
    output = serialize_next_pointers(root)
    print("Output:", output)
