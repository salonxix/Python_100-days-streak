from typing import List

def generate_parentheses(n: int) -> List[str]:
    result = []

    def backtrack(current: str, open_count: int, close_count: int):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result

# Example usage
if __name__ == "__main__":
    try:
        n = int(input("Enter number of parenthesis pairs (n): "))
        combinations = generate_parentheses(n)
        print("\nAll valid combinations:")
        for comb in combinations:
            print(comb)
    except ValueError:
        print("Please enter a valid integer.")
