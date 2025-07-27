def maximumGain(s: str, x: int, y: int) -> int:
    def remove_pattern(s, first, second, points):
        stack = []
        score = 0
        for char in s:
            if stack and stack[-1] == first and char == second:
                stack.pop()
                score += points
            else:
                stack.append(char)
        return "".join(stack), score

    total = 0
    # Remove higher-point pattern first
    if x > y:
        s, gain1 = remove_pattern(s, 'a', 'b', x)
        _, gain2 = remove_pattern(s, 'b', 'a', y)
    else:
        s, gain1 = remove_pattern(s, 'b', 'a', y)
        _, gain2 = remove_pattern(s, 'a', 'b', x)

    return gain1 + gain2

# Test cases
print(maximumGain("cdbcbbaaabab", 4, 5))         # Output: 19
print(maximumGain("aabbaaxybbaabb", 5, 4))       # Output: 20
