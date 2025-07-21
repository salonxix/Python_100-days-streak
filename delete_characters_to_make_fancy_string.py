def makeFancyString(s):
    result = []
    count = 1  # To count repeated characters

    for i in range(len(s)):
        if i > 0 and s[i] == s[i - 1]:
            count += 1
        else:
            count = 1

        if count < 3:
            result.append(s[i])

    return ''.join(result)

# 🔧 Example tests
print(makeFancyString("leeetcode"))  # Output: "leetcode"
print(makeFancyString("aaabaaaa"))   # Output: "aabaa"
print(makeFancyString("aab"))        # Output: "aab"
