def minimumLengthEncoding(words):
    # Step 1: Convert words to a set (to remove duplicates)
    word_set = set(words)

    # Step 2: Remove all words that are suffixes of another word
    for word in words:
        for i in range(1, len(word)):
            suffix = word[i:]
            if suffix in word_set:
                word_set.remove(suffix)

    # Step 3: For remaining words, each needs length + 1 (for '#')
    return sum(len(word) + 1 for word in word_set)


# ---- Test Cases ----
if __name__ == "__main__":
    words1 = ["time", "me", "bell"]
    print(minimumLengthEncoding(words1))  # Expected: 10 ("time#bell#")

    words2 = ["t"]
    print(minimumLengthEncoding(words2))  # Expected: 2 ("t#")
