def mergeSimilarItems(items1, items2):
    from collections import defaultdict

    weight_map = defaultdict(int)

    for value, weight in items1:
        weight_map[value] += weight

    for value, weight in items2:
        weight_map[value] += weight

    # Convert to list and sort by value
    result = sorted([[val, weight] for val, weight in weight_map.items()])
    return result

# 🔧 Example tests
print(mergeSimilarItems([[1,1],[4,5],[3,8]], [[3,1],[1,5]]))  # Output: [[1,6],[3,9],[4,5]]
print(mergeSimilarItems([[1,1],[3,2],[2,3]], [[2,1],[3,2],[1,3]]))  # Output: [[1,4],[2,4],[3,4]]
print(mergeSimilarItems([[1,3],[2,2]], [[7,1],[2,2],[1,4]]))  # Output: [[1,7],[2,4],[7,1]]
