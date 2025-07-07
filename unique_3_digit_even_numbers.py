from collections import Counter

def count_even_3digit_numbers(digits):
    digit_count = Counter(digits)
    valid_numbers = set()

    for num in range(100, 1000):
        if num % 2 == 0:  # Must be even
            num_digits = list(map(int, str(num)))
            temp_count = Counter(num_digits)

            if all(temp_count[d] <= digit_count[d] for d in temp_count):
                valid_numbers.add(num)

    return len(valid_numbers)

# Test cases
print(count_even_3digit_numbers([1, 2, 3, 4]))    # Output: 12
print(count_even_3digit_numbers([0, 2, 2]))       # Output: 2
print(count_even_3digit_numbers([6, 6, 6]))       # Output: 1
print(count_even_3digit_numbers([1, 3, 5]))       # Output: 0
