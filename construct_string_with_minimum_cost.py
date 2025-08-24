def minCostToTarget(target, words, costs):
    n = len(target)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # cost to form empty string is 0

    for i in range(1, n + 1):
        for w, c in zip(words, costs):
            lw = len(w)
            if i >= lw and target[i-lw:i] == w:
                dp[i] = min(dp[i], dp[i-lw] + c)

    return dp[n] if dp[n] != float('inf') else -1


# Example runs
print(minCostToTarget("abcdef", ["abdef","abc","d","def","ef"], [100,1,1,10,5]))
# Output: 7

print(minCostToTarget("aaaa", ["z","zz","zzz"], [1,10,100]))
# Output: -1
