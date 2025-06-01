def is_valid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():  # opening brackets
            stack.append(char)
        elif char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            return False  # invalid character

    return not stack

# Example usage
if __name__ == "__main__":
    s = input("Enter the bracket string: ")
    print("Valid" if is_valid(s) else "Invalid")
