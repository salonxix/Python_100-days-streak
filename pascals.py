from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        for i in range(numRows):
            row = [1] * (i + 1)  # Start and end with 1
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)
        
        return result

if __name__ == "__main__":
    sol = Solution()
    numRows = 5
    triangle = sol.generate(numRows)
    print("Pascal's Triangle:")
    for row in triangle:
        print(row)
