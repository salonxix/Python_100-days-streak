import heapq

def maxEvents(events):
    events.sort()  # sort by start day
    min_heap = []
    i = 0
    res = 0
    day = 1
    n = len(events)

    while i < n or min_heap:
        if not min_heap:
            day = events[i][0]
        
        # Add all events starting today
        while i < n and events[i][0] == day:
            heapq.heappush(min_heap, events[i][1])
            i += 1

        # Remove all events that have already expired
        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)

        if min_heap:
            heapq.heappop(min_heap)  # attend the one that ends earliest
            res += 1

        day += 1

    return res

# Example Usage:
events1 = [[1,2],[2,3],[3,4]]
print("Output:", maxEvents(events1))  # Output: 3

events2 = [[1,2],[2,3],[3,4],[1,2]]
print("Output:", maxEvents(events2))  # Output: 4
