from collections import Counter

def minCost(basket1, basket2):
    # Step 1: Count all fruits
    count1 = Counter(basket1)
    count2 = Counter(basket2)
    total_count = count1 + count2

    # Step 2: Check if possible (all even counts)
    for fruit, total in total_count.items():
        if total % 2 != 0:
            return -1

    # Step 3: Find extra fruits in each basket
    extra1, extra2 = [], []
    for fruit in total_count:
        diff = count1[fruit] - count2[fruit]
        if diff > 0:
            extra1.extend([fruit] * (diff // 2))
        elif diff < 0:
            extra2.extend([fruit] * (-diff // 2))

    # Step 4: Sort extras
    extra1.sort()
    extra2.sort(reverse=True)  # Reverse to pair smallest with largest

    # Step 5: Find minimum swap cost
    min_fruit = min(total_count.keys())
    cost = 0
    for a, b in zip(extra1, extra2):
        cost += min(min(a, b), 2 * min_fruit)

    return cost


# Example Runs
print(minCost([4,2,2,2], [1,4,1,2]))  # Output: 1
print(minCost([2,3,4,1], [3,2,5,1]))  # Output: -1
