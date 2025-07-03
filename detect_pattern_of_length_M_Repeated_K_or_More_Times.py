def containsPattern(arr, m, k):
    n = len(arr)
    
    for i in range(n - m * k + 1):  # ensures we have enough length left to form k patterns
        match = True
        pattern = arr[i:i + m]
        
        for j in range(1, k):
            if arr[i + j * m : i + (j + 1) * m] != pattern:
                match = False
                break
        
        if match:
            return True
            
    return False

# Test Cases
print(containsPattern([1, 2, 4, 4, 4, 4], 1, 3))       # True
print(containsPattern([1, 2, 1, 2, 1, 1, 1, 3], 2, 2)) # True
print(containsPattern([1, 2, 1, 2, 1, 3], 2, 3))       # False
