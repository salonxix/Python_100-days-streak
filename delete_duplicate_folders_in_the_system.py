from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.serial = ""
        self.to_delete = False

def deleteDuplicateFolder(paths):
    root = TrieNode()

    # Step 1: Build Trie
    for path in paths:
        node = root
        for name in path:
            if name not in node.children:
                node.children[name] = TrieNode()
            node = node.children[name]

    # Step 2: Post-order serialize each subtree
    serial_map = defaultdict(list)

    def serialize(node):
        if not node.children:
            return ""
        parts = []
        for name in sorted(node.children):
            child_serial = serialize(node.children[name])
            parts.append(f"{name}({child_serial})")
        node.serial = "".join(parts)
        serial_map[node.serial].append(node)
        return node.serial

    serialize(root)

    # Step 3: Mark duplicate subtrees for deletion
    for nodes in serial_map.values():
        if len(nodes) > 1:
            for node in nodes:
                node.to_delete = True

    # Step 4: Collect paths from unmarked nodes
    result = []

    def collect_paths(node, path):
        for name, child in node.children.items():
            if not child.to_delete:
                result.append(path + [name])
                collect_paths(child, path + [name])

    collect_paths(root, [])
    return result

# 🔧 Example tests
print(deleteDuplicateFolder([["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]))
# Output: [["d"],["d","a"]]

print(deleteDuplicateFolder([["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]))
# Output: [["c"],["c","b"],["a"],["a","b"]]

print(deleteDuplicateFolder([["a","b"],["c","d"],["c"],["a"]]))
# Output: [["c"],["c","d"],["a"],["a","b"]]
