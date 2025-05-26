from collections import defaultdict

def numEquivDominoPairs(dominoes):
    count = defaultdict(int)
    result = 0

    for a, b in dominoes:
        key = tuple(sorted((a, b)))
        result += count[key]
        count[key] += 1

    return result


print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))  
print(numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))  
