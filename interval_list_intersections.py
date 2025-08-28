from typing import List

def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i, j = 0, 0
    result = []

    while i < len(firstList) and j < len(secondList):
        # Find overlap boundaries
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])

        # If valid overlap
        if start <= end:
            result.append([start, end])

        # Move pointer of the interval that ends first
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return result


# Example 1
print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]],
                           [[1,5],[8,12],[15,24],[25,26]]))
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

# Example 2
print(intervalIntersection([[1,3],[5,9]], []))  
# Output: []
