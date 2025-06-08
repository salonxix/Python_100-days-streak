def combine(n: int, k: int):
    result = []
    
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(1, [])
    return result



if __name__ == "__main__":
    n1, k1 = 4, 2
    print("Test Case 1 Output:", combine(n1, k1))  
    # Expected: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    n2, k2 = 1, 1
    print("Test Case 2 Output:", combine(n2, k2))  
    # Expected: [[1]]
