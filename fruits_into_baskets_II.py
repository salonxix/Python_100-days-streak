def unplacedFruits(fruits, baskets):
    n = len(fruits)
    used = [False] * n  # Track used baskets
    unplaced = 0

    for i in range(n):
        placed = False
        for j in range(n):
            if not used[j] and baskets[j] >= fruits[i]:
                used[j] = True
                placed = True
                break
        if not placed:
            unplaced += 1

    return unplaced

# Example usage
print(unplacedFruits([4, 2, 5], [3, 5, 4]))  # Output: 1
print(unplacedFruits([3, 6, 1], [6, 4, 7]))  # Output: 0
