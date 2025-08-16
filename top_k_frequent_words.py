from collections import Counter

def topKFrequent(words, k):
    # Count frequencies
    count = Counter(words)

    # Sort: frequency desc (-count[word]) + lexicographic asc
    sorted_words = sorted(count.keys(), key=lambda word: (-count[word], word))

    # Return first k
    return sorted_words[:k]


# ---- Test Example ----
if __name__ == "__main__":
    words1 = ["i", "love", "leetcode", "i", "love", "coding"]
    k1 = 2
    print(topKFrequent(words1, k1))   # Expected: ["i", "love"]

    words2 = ["the", "day", "is", "sunny", "the", "the", "the", 
              "sunny", "is", "is"]
    k2 = 4
    print(topKFrequent(words2, k2))   # Expected: ["the", "is", "sunny", "day"]
