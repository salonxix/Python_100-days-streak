from collections import defaultdict
import heapq

def findItinerary(tickets):
    graph = defaultdict(list)

    # Build the graph with min-heaps for lexical order
    for src, dst in tickets:
        heapq.heappush(graph[src], dst)

    path = []

    def dfs(node):
        while graph[node]:
            next_dest = heapq.heappop(graph[node])
            dfs(next_dest)
        path.append(node)  # post-order insertion

    dfs("JFK")
    return path[::-1]  # reverse to get correct order

# 🔹 Terminal Test Block
if __name__ == "__main__":
    # Example 1
    tickets1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print("Example 1 Output:", findItinerary(tickets1))  # Expected: ["JFK","MUC","LHR","SFO","SJC"]

    # Example 2
    tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],
                ["ATL","JFK"],["ATL","SFO"]]
    print("Example 2 Output:", findItinerary(tickets2))  # Expected: ["JFK","ATL","JFK","SFO","ATL","SFO"]
