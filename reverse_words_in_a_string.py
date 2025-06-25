# reverse_words.py

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return ' '.join(words[::-1])

# 🧪 Test Cases
if __name__ == "__main__":
    sol = Solution()
    print("Output 1:", sol.reverseWords("the sky is blue"))         # Output: "blue is sky the"
    print("Output 2:", sol.reverseWords("  hello world  "))         # Output: "world hello"
    print("Output 3:", sol.reverseWords("a good   example"))        # Output: "example good a"
