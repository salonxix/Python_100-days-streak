from typing import List

def plusOne(digits: List[int]) -> List[int]:
    n = len(digits)
    
    for i in range(n - 1, -1, -1):
        # If current digit is less than 9, just add one and return
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If it's 9, set it to 0 and continue
        digits[i] = 0

    # If all digits were 9, result is one more digit with 1 followed by all 0s
    return [1] + [0] * n

# Example usage
if __name__ == "__main__":
    try:
        input_str = input("Enter digits separated by commas (e.g., 1,2,3): ")
        digits = list(map(int, input_str.strip().split(',')))
        result = plusOne(digits)
        print("Result after adding one:", result)
    except ValueError:
        print("Invalid input. Please enter digits separated by commas.")
