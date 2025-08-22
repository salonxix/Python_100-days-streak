class Solution:
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        
        # heights[j] will store consecutive ones ending at current row
        heights = [0] * n
        ans = 0
        
        for i in range(m):
            for j in range(n):
                # if cell has 1, add to height, else reset
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # For each row, calculate rectangles ending at this row
            stack = []
            count = [0] * n
            for j in range(n):
                # maintain increasing stack of heights
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()
                if stack:
                    prev_index = stack[-1]
                    count[j] = count[prev_index] + heights[j] * (j - prev_index)
                else:
                    count[j] = heights[j] * (j + 1)
                stack.append(j)
                ans += count[j]
        
        return ans
