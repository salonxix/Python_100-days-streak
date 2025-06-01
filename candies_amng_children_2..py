def count_ways(n: int, limit: int) -> int:
    count = 0

    for i in range(min(n, limit) + 1):
        for j in range(min(n - i, limit) + 1):
            k = n - i - j
            if 0 <= k <= limit:
                count += 1
    return count

# Take input from user
if __name__ == "__main__":
    try:
        n = int(input("Enter total number of candies (n): "))
        limit = int(input("Enter maximum candies per child (limit): "))
        result = count_ways(n, limit)
        print(f"\nTotal number of ways to distribute {n} candies with limit {limit}: {result}")
    except ValueError:
        print("Please enter valid integers for both inputs.")
