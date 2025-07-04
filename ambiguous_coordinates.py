def ambiguousCoordinates(s):
    def valid_nums(part):
        results = []
        n = len(part)
        # If the string itself is valid
        if part == "0" or (part[0] != "0"):
            results.append(part)
        if n > 1 and part[0] != '0':
            for i in range(1, n):
                left, right = part[:i], part[i:]
                if right[-1] != '0':
                    results.append(left + '.' + right)
        elif n > 1 and part[0] == '0':
            if part[-1] != '0':
                results.append('0.' + part[1:])
        return results

    s = s[1:-1]  # remove outer parentheses
    res = []
    for i in range(1, len(s)):
        left, right = s[:i], s[i:]
        left_parts = valid_nums(left)
        right_parts = valid_nums(right)
        for lp in left_parts:
            for rp in right_parts:
                res.append(f"({lp}, {rp})")
    return res

# Example test cases
print(ambiguousCoordinates("(123)"))      # ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"]
print(ambiguousCoordinates("(0123)"))     # ["(0, 1.23)", "(0, 12.3)", "(0, 123)", "(0.1, 2.3)", "(0.1, 23)", "(0.12, 3)"]
print(ambiguousCoordinates("(00011)"))    # ["(0, 0.011)", "(0.001, 1)"]
