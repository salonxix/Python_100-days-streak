def maxFruits(fruits, startPos, k):
    positions = [p for p, _ in fruits]
    amounts = [a for _, a in fruits]

    # Prefix sum for fruit amounts
    prefix = [0]
    for a in amounts:
        prefix.append(prefix[-1] + a)

    n = len(fruits)
    left = 0
    max_fruits = 0

    for right in range(n):
        # Shrink window if both movement patterns exceed k
        while left <= right:
            left_first = (startPos - positions[left]) + (positions[right] - positions[left])
            right_first = (positions[right] - startPos) + (positions[right] - positions[left])
            if min(left_first, right_first) <= k:
                break
            left += 1

        # Fruits in current window
        if left <= right:
            total = prefix[right + 1] - prefix[left]
            max_fruits = max(max_fruits, total)

    return max_fruits


# Example Runs
print(maxFruits([[2,8],[6,3],[8,6]], 5, 4))  # Output: 9
print(maxFruits([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], 5, 4))  # Output: 14
print(maxFruits([[0,3],[6,4],[8,5]], 3, 2))  # Output: 0
