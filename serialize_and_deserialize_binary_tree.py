class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        res = []
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        def dfs():
            val = next(vals)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        vals = iter(data.split(","))
        return dfs()

# 🔸 Test: Construct the tree [1, 2, 3, None, None, 4, 5]
def build_test_tree():
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.right = TreeNode(3)
    node.right.left = TreeNode(4)
    node.right.right = TreeNode(5)
    return node

# 🔹 Main execution for terminal
if __name__ == "__main__":
    codec = Codec()
    root = build_test_tree()

    # Serialize the tree
    serialized = codec.serialize(root)
    print("Serialized Tree:", serialized)

    # Deserialize the string back to tree
    deserialized_root = codec.deserialize(serialized)

    # Print deserialized tree using preorder traversal
    def print_preorder(node):
        if not node:
            print("N", end=' ')
            return
        print(node.val, end=' ')
        print_preorder(node.left)
        print_preorder(node.right)

    print("Deserialized Tree Preorder:", end=" ")
    print_preorder(deserialized_root)
    print()
