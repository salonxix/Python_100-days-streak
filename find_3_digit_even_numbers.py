def findEvenNumbers(digits):
    result = set()
    n = len(digits)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if digits[i] != 0 and num % 2 == 0:
                        result.add(num)

    return sorted(result)

# 🔍 Test Cases
print(findEvenNumbers([2, 1, 3, 0]))       # Output: [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
print(findEvenNumbers([2, 2, 8, 8, 2]))    # Output: [222, 228, 282, 288, 822, 828, 882]
print(findEvenNumbers([3, 7, 5]))          # Output: []
