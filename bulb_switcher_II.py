def flipLights(n: int, presses: int) -> int:
    if presses == 0:
        return 1
    if n > 6:
        n = 6  # patterns repeat every 6 bulbs

    seen = set()
    for b1 in (0, 1):
        for b2 in (0, 1):
            for b3 in (0, 1):
                for b4 in (0, 1):
                    total = b1 + b2 + b3 + b4
                    if total % 2 == presses % 2 and total <= presses:
                        bulbs = [1] * n
                        for i in range(n):
                            if b1:
                                bulbs[i] ^= 1
                            if b2 and (i + 1) % 2 == 0:
                                bulbs[i] ^= 1
                            if b3 and (i + 1) % 2 == 1:
                                bulbs[i] ^= 1
                            if b4 and (i) % 3 == 0:
                                bulbs[i] ^= 1
                        seen.add(tuple(bulbs))
    return len(seen)

# Example usage:
print(flipLights(1, 1))  # Output: 2
print(flipLights(2, 1))  # Output: 3
print(flipLights(3, 1))  # Output: 4
