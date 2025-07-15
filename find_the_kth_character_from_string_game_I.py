def find_kth_character(k):
    word = ["a"]
    
    while len(word) < k:
        # Generate next characters
        next_chars = [chr(((ord(ch) - ord('a') + 1) % 26) + ord('a')) for ch in word]
        word.extend(next_chars)
    
    return word[k - 1]

# 🚀 Example usage
print(find_kth_character(5))   # Output: "b"
print(find_kth_character(10))  # Output: "c"
