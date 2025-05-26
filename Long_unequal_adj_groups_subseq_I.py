def longest_alternating_subsequence(words, groups):
    n = len(words)
    if n == 0:
        return []
    
    # Result list to store the longest alternating subsequence
    result = [words[0]]
    prev_group = groups[0]
    
    for i in range(1, n):
        # Only add if current group's value differs from previous
        if groups[i] != prev_group:
            result.append(words[i])
            prev_group = groups[i]
    
    return result


# Test cases
print(longest_alternating_subsequence(["e","a","b"], [0,0,1]))  # Output: ["e","b"] or ["a","b"]
print(longest_alternating_subsequence(["a","b","c","d"], [1,0,1,1]))  # Output: ["a","b","c"] or ["a","b","d"]
