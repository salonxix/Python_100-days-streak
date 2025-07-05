def greatestLetter(s: str) -> str:
    for ch in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        if ch in s and ch.lower() in s:
            return ch
    return ""

# 🔍 Test Cases
print(greatestLetter("lEeTcOdE"))     # Output: "E"
print(greatestLetter("arRAzFif"))     # Output: "R"
print(greatestLetter("AbCdEfGhIjK"))  # Output: ""
