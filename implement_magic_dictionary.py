class MagicDictionary:
    def __init__(self):
        self.words = []

    def buildDict(self, dictionary):
        """Stores the dictionary words."""
        self.words = dictionary

    def search(self, searchWord):
        """Checks if exactly one character change makes searchWord a dictionary word."""
        for word in self.words:
            # Length must match
            if len(word) != len(searchWord):
                continue
            # Count differences
            diff_count = sum(1 for a, b in zip(word, searchWord) if a != b)
            if diff_count == 1:
                return True
        return False

# ---------------- Example Run ----------------
magicDictionary = MagicDictionary()
magicDictionary.buildDict(["hello", "leetcode"])

print(magicDictionary.search("hello"))      # False
print(magicDictionary.search("hhllo"))      # True
print(magicDictionary.search("hell"))       # False
print(magicDictionary.search("leetcoded"))  # False
