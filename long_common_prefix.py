def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0]  # Start with the first word as the prefix

    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # Shorten prefix by one character
            if not prefix:
                return ""
    return prefix

# User input section to test in VS Code
if __name__ == "__main__":
    strs = input("Enter strings separated by commas: ").split(",")
    print("Longest Common Prefix:", longestCommonPrefix(strs))
