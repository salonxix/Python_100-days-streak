import random
import string

def generate_password(length=12, complexity='medium'):
    if complexity == 'easy':
        chars = string.ascii_lowercase
    elif complexity == 'medium':
        chars = string.ascii_letters + string.digits
    elif complexity == 'hard':
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level!"

    return ''.join(random.choice(chars) for _ in range(length))

# Example usage:
print("Easy password:", generate_password(8, 'easy'))
print("Medium password:", generate_password(12, 'medium'))
print("Hard password:", generate_password(16, 'hard'))
