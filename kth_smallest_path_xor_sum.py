from collections import defaultdict

def subtreeXorQueries(par, vals, queries):
    n = len(par)
    tree = defaultdict(list)
    
    # Step 1: Build Tree
    for i in range(1, n):
        tree[par[i]].append(i)

    # Step 2: DFS to compute path XORs
    path_xor = [0] * n
    def dfs_xor(node, xor_val):
        path_xor[node] = xor_val ^ vals[node]
        for child in tree[node]:
            dfs_xor(child, path_xor[node])

    dfs_xor(0, 0)

    # Step 3: DFS to collect all XORs in each node's subtree
    subtree_xors = defaultdict(set)
    def dfs_subtree(node):
        # narvetholi stores XORs in current subtree
        narvetholi = set()
        narvetholi.add(path_xor[node])
        for child in tree[node]:
            narvetholi.update(dfs_subtree(child))
        subtree_xors[node] = sorted(narvetholi)
        return narvetholi

    dfs_subtree(0)

    # Step 4: Answer Queries
    result = []
    for u, k in queries:
        if k <= len(subtree_xors[u]):
            result.append(subtree_xors[u][k - 1])
        else:
            result.append(-1)
    return result


# 🔍 Example usage:
print(subtreeXorQueries(par=[-1,0,0], vals=[1,1,1], queries=[[0,1],[0,2],[0,3]]))  
# Output: [0,1,-1]

print(subtreeXorQueries(par=[-1,0,1], vals=[5,2,7], queries=[[0,1],[1,2],[1,3],[2,1]]))  
# Output: [0,7,-1,0]
