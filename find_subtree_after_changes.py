from collections import defaultdict

def subtreeSizesAfterReparenting(parent, s):
    n = len(parent)
    tree = defaultdict(list)

    # Build the original tree
    for i in range(1, n):
        tree[parent[i]].append(i)

    # Step 1: Store nearest ancestors with same char using a stack per character
    new_parent = parent[:]  # Copy the original parent array
    char_stack = defaultdict(list)

    def dfs1(node):
        char_stack[s[node]].append(node)
        for child in tree[node]:
            # Before diving in, look for same-char ancestor
            if len(char_stack[s[child]]) > 0:
                # Closest same-char ancestor is top of stack
                new_parent[child] = char_stack[s[child]][-1]
            dfs1(child)
        char_stack[s[node]].pop()

    dfs1(0)

    # Step 2: Rebuild the new tree
    new_tree = defaultdict(list)
    for i in range(1, n):
        new_tree[new_parent[i]].append(i)

    # Step 3: Compute subtree sizes
    result = [0] * n

    def dfs2(node):
        size = 1
        for child in new_tree[node]:
            size += dfs2(child)
        result[node] = size
        return size

    dfs2(0)
    return result

# ✅ Example 1
parent1 = [-1,0,0,1,1,1]
s1 = "abaabc"
print(subtreeSizesAfterReparenting(parent1, s1))  # ➤ [6,3,1,1,1,1]

# ✅ Example 2
parent2 = [-1,0,4,0,1]
s2 = "abbba"
print(subtreeSizesAfterReparenting(parent2, s2))  # ➤ [5,2,1,1,1]
