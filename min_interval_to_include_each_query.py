import heapq

def minInterval(intervals, queries):
    # Sort intervals by start
    intervals.sort()
    # Keep queries with their original index
    sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])
    
    result = [-1] * len(queries)
    heap = []  # (interval_size, interval_end)
    i = 0  # pointer for intervals
    
    for q, idx in sorted_queries:
        # Add all intervals that start <= query
        while i < len(intervals) and intervals[i][0] <= q:
            start, end = intervals[i]
            size = end - start + 1
            heapq.heappush(heap, (size, end))
            i += 1
        
        # Remove intervals that end < query (not valid)
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        
        # If valid interval exists, assign result
        if heap:
            result[idx] = heap[0][0]
    
    return result


# ✅ Example Tests
print(minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]))  
# Output: [3,3,1,4]

print(minInterval([[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]))  
# Output: [2,-1,4,6]
