def longestWord(words):
    # Sort words: first by length (asc), then lexicographically
    words.sort()
    
    # Set to keep track of valid words we can build
    valid = set([""])  # empty string is the base
    
    longest = ""
    
    for word in words:
        # Check if prefix (word[:-1]) exists in valid
        if word[:-1] in valid:
            valid.add(word)  # add to valid words
            # Update longest if needed
            if len(word) > len(longest):
                longest = word
    
    return longest


# ---- Test Example ----
if __name__ == "__main__":
    words1 = ["w","wo","wor","worl","world"]
    print(longestWord(words1))   # Expected: "world"

    words2 = ["a","banana","app","appl","ap","apply","apple"]
    print(longestWord(words2))   # Expected: "apple"
