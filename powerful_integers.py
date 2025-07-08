def powerfulIntegers(x, y, bound):
    result = set()
    i = 0
    while x ** i <= bound:
        j = 0
        while x ** i + y ** j <= bound:
            result.add(x ** i + y ** j)
            if y == 1:
                break
            j += 1
        if x == 1:
            break
        i += 1
    return list(result)

# 🔍 Test Cases
print(powerfulIntegers(2, 3, 10))  # Output: [2, 3, 4, 5, 7, 9, 10]
print(powerfulIntegers(3, 5, 15))  # Output: [2, 4, 6, 8, 10, 14]
print(powerfulIntegers(1, 1, 2))   # Output: [2]
