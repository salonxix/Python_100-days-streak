# clone_graph_runner.py

from typing import List, Dict

# Node class definition
class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Solution with DFS to clone graph
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        visited: Dict[Node, Node] = {}

        def dfs(curr: 'Node') -> 'Node':
            if curr in visited:
                return visited[curr]

            clone = Node(curr.val)
            visited[curr] = clone

            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)

# Helper function to print a graph (DFS)
def print_graph(node: 'Node', visited=set()):
    if node.val in visited:
        return
    visited.add(node.val)
    neighbors_vals = [n.val for n in node.neighbors]
    print(f"Node {node.val} -> Neighbors: {neighbors_vals}")
    for neighbor in node.neighbors:
        print_graph(neighbor, visited)

# Graph creation and testing
if __name__ == "__main__":
    # Creating a graph with 4 nodes as per example
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    print("🔹 Original Graph:")
    print_graph(n1)

    # Clone the graph
    sol = Solution()
    cloned_graph = sol.cloneGraph(n1)

    print("\n🔸 Cloned Graph:")
    print_graph(cloned_graph)
