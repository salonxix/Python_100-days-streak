def largestString(word: str, numFriends: int) -> str:
    result = set()
    
    def backtrack(start, parts):
        if len(parts) == numFriends:
            if start == len(word):
                result.update(parts)
            return
        
        for end in range(start + 1, len(word) - (numFriends - len(parts) - 1) + 1):
            backtrack(end, parts + [word[start:end]])
    
    backtrack(0, [])
    
    return max(result) if result else ""

# 🔍 Test Cases
print(largestString("dbca", 2))    # Output: "dbc"
print(largestString("gggg", 4))    # Output: "g"
