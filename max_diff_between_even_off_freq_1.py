from collections import Counter

def maxDiffOddEvenFreq(s):
    freq = Counter(s)
    
    odd_freq = [v for v in freq.values() if v % 2 == 1]
    even_freq = [v for v in freq.values() if v % 2 == 0]
    
    if not odd_freq or not even_freq:
        return -1
    
    return max(o - e for o in odd_freq for e in even_freq)

# Example usage
s = "aaaaabbc"
print("Output:", maxDiffOddEvenFreq(s))  # ➤ 3
