# max_points_on_line.py

from collections import defaultdict
from fractions import Fraction

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        max_points = 0

        for i in range(len(points)):
            slope_count = defaultdict(int)
            duplicates = 1  # Count the point itself
            vertical = 0

            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    duplicates += 1
                elif x1 == x2:
                    slope = 'inf'
                    slope_count[slope] += 1
                else:
                    slope = Fraction(y2 - y1, x2 - x1)
                    slope_count[slope] += 1

            current_max = max(slope_count.values(), default=0)
            max_points = max(max_points, current_max + duplicates)

        return max_points

# 🧪 Test Case
if __name__ == "__main__":
    sol = Solution()
    
    points1 = [[1, 1], [2, 2], [3, 3]]
    print("Output 1:", sol.maxPoints(points1))  # Output: 3

    points2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    print("Output 2:", sol.maxPoints(points2))  # Output: 4
