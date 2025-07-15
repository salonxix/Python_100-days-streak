def count_possible_originals(word):
    n = len(word)
    groups = []
    i = 0

    # Step 1: Group consecutive characters
    while i < n:
        j = i
        while j < n and word[j] == word[i]:
            j += 1
        groups.append(j - i)
        i = j

    # Step 2: Count combinations
    total = 1  # original string as-is
    for length in groups:
        if length > 1:
            total += (length - 1)  # remove 1 to length-1 chars from this group
    return total

# 🚀 Example usage
word = "abbcccc"
print("Output:", count_possible_originals(word))
