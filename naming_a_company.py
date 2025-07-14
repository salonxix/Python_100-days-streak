from collections import defaultdict

def distinctNames(ideas):
    groups = [set() for _ in range(26)]

    # Group words by first letter
    for idea in ideas:
        first = ord(idea[0]) - ord('a')
        groups[first].add(idea[1:])  # store suffix

    result = 0
    for i in range(26):
        for j in range(i + 1, 26):
            set1 = groups[i]
            set2 = groups[j]
            # Common suffixes are invalid
            common = len(set1 & set2)
            valid1 = len(set1) - common
            valid2 = len(set2) - common
            result += valid1 * valid2 * 2  # (A,B) and (B,A)

    return result

# 🔽 Sample Inputs
print("Example 1 Output:", distinctNames(["coffee","donuts","time","toffee"]))  # ➤ 6
print("Example 2 Output:", distinctNames(["lack","back"]))                      # ➤ 0
