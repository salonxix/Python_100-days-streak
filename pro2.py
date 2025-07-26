import time
import os
import random

words = ["apple", "river", "dream", "python", "cloud", "sunset", "robot", "glass"]
chosen = random.sample(words, 4)

print("Memorize these words:")
print(", ".join(chosen))
time.sleep(5)

# Clear screen (cross-platform)
os.system('cls' if os.name == 'nt' else 'clear')

print("Enter the words you remember:")
answers = [input(f"Word {i+1}: ") for i in range(4)]

score = sum(1 for w in answers if w in chosen)
print(f"\nYou remembered {score}/4 words correctly!")
