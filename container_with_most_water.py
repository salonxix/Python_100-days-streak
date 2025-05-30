def maxContainer(height):
    i = 0
    j = len(height) - 1
    maxArea = 0
    while i < j:
        
        area = min(height[i], height[j]) * (j - i)
        maxArea = max(maxArea, area)
        
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return maxArea


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxContainer(height))  

height2 = [1, 1]
print(maxContainer(height2))  
