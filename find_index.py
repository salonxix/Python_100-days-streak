def find_needle(haystack: str, needle: str) -> int:
    # Edge case: if needle is empty, return 0 as per problem convention
    if needle == "":
        return 0

    hay_len = len(haystack)
    needle_len = len(needle)

    # We only need to loop until there's enough space left in haystack
    for i in range(hay_len - needle_len + 1):
        match = True  # assume a match

        # Check each character of needle against haystack
        for j in range(needle_len):
            if haystack[i + j] != needle[j]:
                match = False
                break

        if match:
            return i  # return the starting index of match

    # If we complete the loop with no match found
    return -1

# Day 17 Example Test Cases
print(find_needle("sadbutsad", "sad"))     # Output: 0
print(find_needle("leetcode", "leeto"))    # Output: -1
