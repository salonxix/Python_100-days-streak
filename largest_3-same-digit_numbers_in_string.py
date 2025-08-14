def largestGoodInteger(num):
    max_good = ""
    for i in range(len(num) - 2):
        sub = num[i:i+3]
        if sub[0] == sub[1] == sub[2]:  # all same
            if sub > max_good:
                max_good = sub
    return max_good

# Example usage
print(largestGoodInteger("6777133339"))  # "777"
print(largestGoodInteger("2300019"))     # "000"
print(largestGoodInteger("42352338"))    # ""
