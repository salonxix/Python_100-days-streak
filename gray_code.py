def grayCode(n):
    result = []
    for i in range(1 << n):  # 1 << n is 2^n
        gray = i ^ (i >> 1)
        result.append(gray)
    return result

# 🚀 Test Cases
test_cases = [1, 2, 3]

for i, n in enumerate(test_cases):
    output = grayCode(n)
    print(f"Test Case {i+1}: n = {n}")
    print(f"Output Gray Code Sequence: {output}")
    print("Binary Representation:", [format(x, f'0{n}b') for x in output])
    print()
