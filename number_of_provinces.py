# Main Code
class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        province_count = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                province_count += 1

        return province_count

# Example 1
isConnected1 = [[1,1,0],[1,1,0],[0,0,1]]
# Example 2
isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]

sol = Solution()
print("Output for Example 1:", sol.findCircleNum(isConnected1))  # Expected: 2
print("Output for Example 2:", sol.findCircleNum(isConnected2))  # Expected: 3
