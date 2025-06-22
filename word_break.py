# word_break.py

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # base case: empty string

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


# 🔧 Test Examples
if __name__ == "__main__":
    sol = Solution()
    
    print("Test 1:", sol.wordBreak("leetcode", ["leet", "code"]))  # True
    print("Test 2:", sol.wordBreak("applepenapple", ["apple", "pen"]))  # True
    print("Test 3:", sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
