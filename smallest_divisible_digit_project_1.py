

def digit_product(x):
    prod = 1
    for ch in str(x):
        prod *= int(ch)
        if prod == 0:
            return 0
    return prod

def smallest_valid_number(n, t):
    while True:
        if digit_product(n) % t == 0:
            return n
        n += 1

# 🚀 Sample Test Cases
if __name__ == "__main__":
    test_cases = [
        (10, 2, 10),
        (15, 3, 16),
        (1, 1, 1),
        (25, 5, 25),
        (19, 6, 23),  # 2*3 = 6
        (98, 7, 98),  # 9*8 = 72
    ]

    for i, (n, t, expected) in enumerate(test_cases):
        result = smallest_valid_number(n, t)
        print(f"Test Case {i+1}: n = {n}, t = {t}")
        print(f"Expected: {expected}, Got: {result}")
        print("✅ Pass" if result == expected else "❌ Fail", end="\n\n")
