from functools import lru_cache

def maxFreeTime(eventTime, k, startTime, endTime):
    n = len(startTime)
    durations = [endTime[i] - startTime[i] for i in range(n)]

    @lru_cache(None)
    def dp(index, time, k_left):
        if index == n:
            return eventTime - time

        max_gap = 0
        duration = durations[index]

        # Option 1: Don't reschedule this meeting
        if startTime[index] >= time:
            gap = startTime[index] - time
            max_gap = max(max_gap, gap + dp(index + 1, endTime[index], k_left))

        # Option 2: Reschedule if allowed
        if k_left > 0:
            if time + duration <= eventTime:
                max_gap = max(max_gap, dp(index + 1, time + duration, k_left - 1))

        return max_gap

    return dp(0, 0, k)

# Test cases
print("Output 1:", maxFreeTime(5, 1, [1,3], [2,5]))           # Output: 2
print("Output 2:", maxFreeTime(10, 1, [0,2,9], [1,4,10]))     # Output: 6
print("Output 3:", maxFreeTime(5, 2, [0,1,2,3,4], [1,2,3,4,5])) # Output: 0
