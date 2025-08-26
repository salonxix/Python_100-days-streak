# Day 97 - Word Frequency Counter

from collections import Counter

def word_frequency(filename):
    # Read file content
    with open(filename, 'r') as file:
        words = file.read().split()
    
    # Count frequency of words
    freq = Counter(words)
    
    # Sort by frequency (descending), then alphabetically if needed
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # Print results
    for word, count in sorted_freq:
        print(f"{word} {count}")


# Example usage
if __name__ == "__main__":
    word_frequency("words.txt")
