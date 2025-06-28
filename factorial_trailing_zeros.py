def trailingZeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


# ✅ Test Cases
if __name__ == "__main__":
    print(trailingZeroes(3))   # ➤ 0
    print(trailingZeroes(5))   # ➤ 1
    print(trailingZeroes(0))   # ➤ 0
    print(trailingZeroes(100)) # ➤ 24
