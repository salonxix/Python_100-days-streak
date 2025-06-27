def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return "0"

    result = []

    # Sign
    if (numerator < 0) ^ (denominator < 0):
        result.append("-")

    numerator, denominator = abs(numerator), abs(denominator)

    # Integer part
    integer_part = numerator // denominator
    result.append(str(integer_part))
    remainder = numerator % denominator

    if remainder == 0:
        return "".join(result)

    result.append(".")
    remainder_map = {}

    while remainder != 0:
        if remainder in remainder_map:
            insert_pos = remainder_map[remainder]
            result.insert(insert_pos, "(")
            result.append(")")
            break

        remainder_map[remainder] = len(result)
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator

    return "".join(result)


# ✅ Test Cases
if __name__ == "__main__":
    print(fractionToDecimal(1, 2))      # ➤ "0.5"
    print(fractionToDecimal(2, 1))      # ➤ "2"
    print(fractionToDecimal(4, 333))    # ➤ "0.(012)"
    print(fractionToDecimal(1, 6))      # ➤ "0.1(6)"
    print(fractionToDecimal(-50, 8))    # ➤ "-6.25"
