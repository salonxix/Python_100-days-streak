# palindrome_partitioning.py

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int, path: List[str]):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if is_palindrome(prefix):
                    path.append(prefix)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res


# 🔧 Test Example
if __name__ == "__main__":
    sol = Solution()

    s1 = "aab"
    print("Partitions for 'aab':", sol.partition(s1))  # [["a","a","b"],["aa","b"]]

    s2 = "a"
    print("Partitions for 'a':", sol.partition(s2))    # [["a"]]
