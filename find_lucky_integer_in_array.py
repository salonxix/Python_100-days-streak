from collections import Counter

def findLucky(arr):
    freq = Counter(arr)
    max_lucky = -1
    
    for num in freq:
        if freq[num] == num:
            max_lucky = max(max_lucky, num)
    
    return max_lucky

# Example usage
print(findLucky([2, 2, 3, 4]))        # Output: 2
print(findLucky([1, 2, 2, 3, 3, 3]))  # Output: 3
print(findLucky([2, 2, 2, 3, 3]))     # Output: -1
