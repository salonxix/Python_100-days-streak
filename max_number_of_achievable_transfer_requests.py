from itertools import combinations

def maximumRequests(n, requests):
    max_count = 0
    m = len(requests)

    for mask in range(1 << m):
        delta = [0] * n
        count = 0
        for i in range(m):
            if mask & (1 << i):
                from_b, to_b = requests[i]
                delta[from_b] -= 1
                delta[to_b] += 1
                count += 1
        if all(x == 0 for x in delta):
            max_count = max(max_count, count)
    
    return max_count

# Example Usage:
n = 5
requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
print(maximumRequests(n, requests))  # Output: 5
