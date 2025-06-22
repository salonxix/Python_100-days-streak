# word_break_ii.py

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    sub_sentences = backtrack(end)
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
            memo[start] = res
            return res

        return backtrack(0)


# 🔧 Test Examples
if __name__ == "__main__":
    sol = Solution()

    print("Test 1:", sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print("Test 2:", sol.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    print("Test 3:", sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
