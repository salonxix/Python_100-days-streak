def findWordsWithChar(words, x):
    result = []
    for i, word in enumerate(words):
        if x in word:
            result.append(i)
    return result

# Test cases
print(findWordsWithChar(["leet","code"], "e"))       # Output: [0, 1]
print(findWordsWithChar(["abc","bcd","aaaa","cbc"], "a"))  # Output: [0, 2]
print(findWordsWithChar(["abc","bcd","aaaa","cbc"], "z"))  # Output: []
