def sequentialDigits(low, high):
    result = []
    digits = "123456789"

    for length in range(2, 10):  # Length of sequential numbers
        for i in range(0, 10 - length):
            num = int(digits[i:i + length])
            if low <= num <= high:
                result.append(num)

    return sorted(result)


# ---------- DRIVER CODE ----------
if __name__ == "__main__":
    low = int(input("Enter lower bound: "))
    high = int(input("Enter upper bound: "))
    print("Sequential digits in range:", sequentialDigits(low, high))
