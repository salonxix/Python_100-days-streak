import heapq

def getSkyline(buildings):
    # Step 1: Create events for building start and end
    events = []
    for left, right, height in buildings:
        events.append((left, -height, right))  # building start
        events.append((right, 0, 0))           # building end marker
    
    # Step 2: Sort events by x position
    events.sort()
    
    # Step 3: Max heap to keep track of active buildings
    result = []
    heap = [(0, float('inf'))]  # (negative height, right boundary)
    prev_height = 0
    
    for x, neg_h, r in events:
        # Remove buildings that ended before current x
        while heap and heap[0][1] <= x:
            heapq.heappop(heap)
        
        if neg_h:  # building start
            heapq.heappush(heap, (neg_h, r))
        
        # Current tallest height
        curr_height = -heap[0][0]
        
        # If height changes, add to result
        if curr_height != prev_height:
            result.append([x, curr_height])
            prev_height = curr_height
    
    return result


# Example usage
print(getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print(getSkyline([[0,2,3],[2,5,3]]))
