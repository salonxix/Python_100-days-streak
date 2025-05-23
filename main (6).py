# Day 6 of 100 Days of Python - Word Count Tool

def word_and_char_count(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    return word_count, char_count

print("Word Count Tool")
user_input = input("Enter a sentence or paragraph: ")

words, chars = word_and_char_count(user_input)
print(f"Total Words: {words}")
print(f"Total Characters (including spaces): {chars}")