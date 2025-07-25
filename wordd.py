from collections import Counter

def word_frequency(text):
    words = text.lower().split()
    count = Counter(words)
    for word, freq in count.items():
        print(f"{word}: {freq}")

if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")
    word_frequency(paragraph)
