def lexicalOrder(n):
    result = []

    def dfs(curr):
        if curr > n:
            return
        result.append(curr)
        for i in range(10):
            next_num = curr * 10 + i
            if next_num > n:
                return
            dfs(next_num)

    for i in range(1, 10):
        dfs(i)

    return result

# Input from user
n = int(input("Enter a number: "))
output = lexicalOrder(n)

# Print result
print("Lexicographical order:")
print(output)
