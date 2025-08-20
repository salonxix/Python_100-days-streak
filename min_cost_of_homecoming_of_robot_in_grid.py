class Solution:
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        startRow, startCol = startPos
        homeRow, homeCol = homePos
        totalCost = 0

        # Move row by row toward home
        if startRow < homeRow:
            for r in range(startRow + 1, homeRow + 1):
                totalCost += rowCosts[r]
        else:
            for r in range(startRow - 1, homeRow - 1, -1):
                totalCost += rowCosts[r]

        # Move column by column toward home
        if startCol < homeCol:
            for c in range(startCol + 1, homeCol + 1):
                totalCost += colCosts[c]
        else:
            for c in range(startCol - 1, homeCol - 1, -1):
                totalCost += colCosts[c]

        return totalCost
