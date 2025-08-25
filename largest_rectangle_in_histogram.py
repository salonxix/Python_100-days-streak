def largestRectangleArea(heights):
    stack = []  # stack to store indices
    max_area = 0
    n = len(heights)

    for i in range(n):
        # while stack not empty and current bar is smaller than top of stack
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    # handle remaining bars in stack
    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area


# Example Runs
print(largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
print(largestRectangleArea([2,4]))          # Output: 4
