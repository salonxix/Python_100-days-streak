from collections import defaultdict

def calcEquation(equations, values, queries):
    graph = defaultdict(dict)

    # Step 1: Build the graph
    for (a, b), val in zip(equations, values):
        graph[a][b] = val
        graph[b][a] = 1 / val

    # Step 2: DFS to evaluate queries
    def dfs(start, end, visited):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)

        for neighbor, val in graph[start].items():
            if neighbor in visited:
                continue
            result = dfs(neighbor, end, visited)
            if result != -1.0:
                return val * result

        return -1.0

    results = []
    for a, b in queries:
        results.append(dfs(a, b, set()))

    return results

# Terminal Input
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

output = calcEquation(equations, values, queries)
print("Query results:", output)
