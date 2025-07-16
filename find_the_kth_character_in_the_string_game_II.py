def getKthCharacter(k, operations):
    word = ["a"]

    for op in operations:
        if op == 0:
            word += word  # Append a copy
        elif op == 1:
            next_chars = [chr(((ord(c) - ord('a') + 1) % 26) + ord('a')) for c in word]
            word += next_chars  # Append next-letter version

        if len(word) >= k:
            break  # Stop early if we already have enough characters

    return word[k - 1]

# 🚀 Example usage
print(getKthCharacter(5, [0, 0, 0]))       # Output: "a"
print(getKthCharacter(10, [0, 1, 0, 1]))   # Output: "b"
