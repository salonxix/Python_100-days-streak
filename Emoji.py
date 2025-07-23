def emoji_translator(text):
    emoji_dict = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😡",
        "love": "❤️",
        "cool": "😎",
        "fire": "🔥",
        "star": "⭐",
        "cry": "😭",
        "hello": "👋",
        "ok": "👌"
    }
    words = text.lower().split()
    translated = [emoji_dict.get(word, word) for word in words]
    return ' '.join(translated)

# Example usage:
sentence = "hello I am feeling happy and cool today"
print("Original:", sentence)
print("Emoji Version:", emoji_translator(sentence))
