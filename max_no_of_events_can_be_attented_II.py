from functools import lru_cache
import bisect

def maxValue(events, k):
    # Sort events by start day
    events.sort()
    starts = [e[0] for e in events]
    n = len(events)

    @lru_cache(None)
    def dp(i, remaining):
        if i == n or remaining == 0:
            return 0
        
        # Binary search to find the next non-overlapping event
        next_i = bisect.bisect_right(starts, events[i][1])
        
        # Option 1: skip this event
        skip = dp(i + 1, remaining)
        
        # Option 2: take this event
        take = events[i][2] + dp(next_i, remaining - 1)

        return max(skip, take)

    return dp(0, k)

# Example Usage
events1 = [[1,2,4],[3,4,3],[2,3,1]]
print("Output:", maxValue(events1, 2))  # Output: 7

events2 = [[1,2,4],[3,4,3],[2,3,10]]
print("Output:", maxValue(events2, 2))  # Output: 10

events3 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
print("Output:", maxValue(events3, 3))  # Output: 9
