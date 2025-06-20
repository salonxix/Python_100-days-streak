# palindrome_partitioning_ii.py

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False]*n for _ in range(n)]

        # Precompute palindromes
        for i in range(n):
            is_palindrome[i][i] = True
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        is_palindrome[i][j] = True
                    else:
                        is_palindrome[i][j] = is_palindrome[i+1][j-1]

        # DP to find min cut
        dp = [0]*n
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = i  # max cuts
                for j in range(i):
                    if is_palindrome[j+1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[n-1]


# 🔧 Test Examples
if __name__ == "__main__":
    sol = Solution()
    print("Min cuts for 'aab':", sol.minCut("aab"))  # Output: 1
    print("Min cuts for 'a':", sol.minCut("a"))      # Output: 0
    print("Min cuts for 'ab':", sol.minCut("ab"))    # Output: 1
