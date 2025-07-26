def countAlternatingGroups(colors):
    n = len(colors)
    count = 0

    for i in range(n):
        left = colors[i - 1]
        middle = colors[i]
        right = colors[(i + 1) % n]
        
        if left != middle and right != middle and left == right:
            count += 1

    return count

# Test cases
print("Example 1 Output:", countAlternatingGroups([1, 1, 1]))         # Output: 0
print("Example 2 Output:", countAlternatingGroups([0, 1, 0, 0, 1]))   # Output: 3
