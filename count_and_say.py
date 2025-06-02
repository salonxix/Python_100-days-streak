def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    
    prev = countAndSay(n - 1)
    result = ""
    count = 1

    for i in range(1, len(prev)):
        if prev[i] == prev[i - 1]:
            count += 1
        else:
            result += str(count) + prev[i - 1]
            count = 1
    result += str(count) + prev[-1]
    
    return result

# Example usage
if __name__ == "__main__":
    n = int(input("Enter n: "))
    print("Count and Say sequence at position", n, "is:", countAndSay(n))
