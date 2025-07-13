from bisect import bisect_right
from itertools import accumulate

def maxBeauty(flowers, newFlowers, target, full, partial):
    n = len(flowers)
    flowers = [min(f, target) for f in flowers]
    flowers.sort()
    prefix = [0] + list(accumulate(flowers))
    
    def min_partial(l, r, rem):
        # Maximize min value for [0, r)
        low, high = flowers[0], target - 1
        res = 0
        while low <= high:
            mid = (low + high) // 2
            idx = bisect_right(flowers, mid, 0, r)
            need = mid * idx - prefix[idx]
            if need <= rem:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res

    max_beauty = 0
    for complete in range(n + 1):
        # Number of full gardens = complete
        rem = newFlowers
        # Cost to make last 'complete' gardens full
        for i in range(n - complete, n):
            rem -= max(0, target - flowers[i])
        if rem < 0:
            continue
        if complete == n:
            max_beauty = max(max_beauty, full * n)
        else:
            min_val = min_partial(0, n - complete, rem)
            max_beauty = max(max_beauty, complete * full + min_val * partial)
    return max_beauty

# 🔽 Sample Inputs
print("Example 1 Output:", maxBeauty([1,3,1,1], 7, 6, 12, 1))  # ➤ 14
print("Example 2 Output:", maxBeauty([2,4,5,3], 10, 5, 2, 6))  # ➤ 30
