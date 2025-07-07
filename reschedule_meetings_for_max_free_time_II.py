def maxFreeTime(eventTime, startTime, endTime):
    n = len(startTime)
    intervals = sorted(zip(startTime, endTime))
    
    def get_free_time(slots):
        free = []
        if slots[0][0] > 0:
            free.append((0, slots[0][0]))
        for i in range(1, len(slots)):
            if slots[i][0] > slots[i-1][1]:
                free.append((slots[i-1][1], slots[i][0]))
        if slots[-1][1] < eventTime:
            free.append((slots[-1][1], eventTime))
        return free

    # Get original max free time without any move
    original_free = get_free_time(intervals)
    max_gap = max((e - s for s, e in original_free), default=0)

    # Try rescheduling each meeting to each free slot
    for i in range(n):
        duration = endTime[i] - startTime[i]
        remaining = intervals[:i] + intervals[i+1:]
        current_free = get_free_time(remaining)

        for s, e in current_free:
            if e - s >= duration:
                # Move meeting i to [s, s+duration]
                new_slot = (s, s + duration)
                new_schedule = remaining + [new_slot]
                new_schedule.sort()
                new_free = get_free_time(new_schedule)
                max_gap = max(max_gap, max((x[1] - x[0] for x in new_free), default=0))
    
    return max_gap

# 🔍 Test Cases
print(maxFreeTime(5, [1, 3], [2, 5]))        # Output: 2
print(maxFreeTime(10, [0,7,9], [1,8,10]))    # Output: 7
print(maxFreeTime(10, [0,3,7,9], [1,4,8,10]))# Output: 6
print(maxFreeTime(5, [0,1,2,3,4], [1,2,3,4,5])) # Output: 0
