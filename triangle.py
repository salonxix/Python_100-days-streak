from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second last row and go upwards
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Add the minimum of the two adjacent numbers from below
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

if __name__ == "__main__":
    sol = Solution()
    
    triangle1 = [[2], [3,4], [6,5,7], [4,1,8,3]]
    print("Minimum path sum (Example 1):", sol.minimumTotal(triangle1))  # Output: 11

    triangle2 = [[-10]]
    print("Minimum path sum (Example 2):", sol.minimumTotal(triangle2))  # Output: -10
