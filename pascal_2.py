from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for k in range(1, rowIndex + 1):
            # Compute C(n, k) based on previous value
            value = row[-1] * (rowIndex - k + 1) // k
            row.append(value)
        return row

if __name__ == "__main__":
    sol = Solution()
    rowIndex = 3
    result = sol.getRow(rowIndex)
    print(f"{rowIndex}th row of Pascal's Triangle:")
    print(result)
