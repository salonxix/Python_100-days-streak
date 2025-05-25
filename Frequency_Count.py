text = input("Enter text: ").lower()
freq = {}
for char in text:
    if char.isalpha():
        freq[char] = freq.get(char, 0) + 1
print("Character frequencies:", freq)
