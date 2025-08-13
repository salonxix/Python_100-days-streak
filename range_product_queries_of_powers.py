def productQueries(n: int, queries: list[list[int]]) -> list[int]:
    MOD = 10**9 + 7
    
    # Step 1: Extract powers of 2 from n's binary representation
    powers = []
    bit = 1
    while n > 0:
        if n & 1:
            powers.append(bit)
        bit <<= 1
        n >>= 1
    
    # Step 2: Precompute prefix products modulo MOD
    prefix_prod = [1] * (len(powers) + 1)
    for i in range(len(powers)):
        prefix_prod[i+1] = (prefix_prod[i] * powers[i]) % MOD
    
    # Step 3: Answer queries using prefix product trick
    ans = []
    for left, right in queries:
        product = (prefix_prod[right+1] * pow(prefix_prod[left], MOD-2, MOD)) % MOD
        ans.append(product)
    
    return ans


# Example usage
print(productQueries(15, [[0,1],[2,2],[0,3]]))  # [2, 4, 64]
print(productQueries(2, [[0,0]]))              # [2]
