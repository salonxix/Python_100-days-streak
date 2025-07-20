def maximalRectangle(matrix):
    if not matrix:
        return 0

    cols = len(matrix[0])
    heights = [0] * (cols + 1)  # Add one extra for stack cleanup
    max_area = 0

    for row in matrix:
        for i in range(cols):
            # Update histogram: increase count or reset to 0
            heights[i] = heights[i] + 1 if row[i] == '1' else 0

        stack = [-1]  # Start with dummy index
        for i in range(cols + 1):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

    return max_area

# 🔧 Example tests
print(maximalRectangle([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]))  # Output: 6

print(maximalRectangle([["0"]]))  # Output: 0
print(maximalRectangle([["1"]]))  # Output: 1
