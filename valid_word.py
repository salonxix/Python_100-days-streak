def isValidWord(word):
    if len(word) < 3:
        return False

    vowels = set("aeiouAEIOU")
    has_vowel = False
    has_consonant = False

    for ch in word:
        if not ch.isalnum():
            return False
        if ch.isalpha():
            if ch in vowels:
                has_vowel = True
            else:
                has_consonant = True

    return has_vowel and has_consonant

# Test Cases
print("Input: '234Adas' ->", isValidWord("234Adas"))  # True
print("Input: 'b3' ->", isValidWord("b3"))            # False
print("Input: 'a3$e' ->", isValidWord("a3$e"))         # False
print("Input: 'Ai9' ->", isValidWord("Ai9"))           # True
