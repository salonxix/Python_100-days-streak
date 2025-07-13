def maximumGood(statements):
    n = len(statements)
    max_good = 0

    # Try all subsets of people (bitmask: 1 = good, 0 = bad)
    for mask in range(1 << n):
        valid = True

        for i in range(n):
            if not (mask & (1 << i)):  # If person i is bad, skip
                continue
            for j in range(n):
                if statements[i][j] == 2:
                    continue
                # Good person i says something about j
                expected = statements[i][j]
                actual = 1 if (mask & (1 << j)) else 0
                if expected != actual:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            max_good = max(max_good, bin(mask).count('1'))
    
    return max_good

# 🔽 Sample Inputs
statements1 = [[2,1,2],[1,2,2],[2,0,2]]
statements2 = [[2,0],[0,2]]

print("Example 1 Output:", maximumGood(statements1))  # ➤ 2
print("Example 2 Output:", maximumGood(statements2))  # ➤ 1
