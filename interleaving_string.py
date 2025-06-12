def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
    dp[0][0] = True

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i > 0 and s1[i-1] == s3[i+j-1]:
                dp[i][j] |= dp[i-1][j]
            if j > 0 and s2[j-1] == s3[i+j-1]:
                dp[i][j] |= dp[i][j-1]

    return dp[len(s1)][len(s2)]

# -------- Main Driver --------
if __name__ == "__main__":
    s1 = input("Enter string s1: ")
    s2 = input("Enter string s2: ")
    s3 = input("Enter string s3: ")

    result = isInterleave(s1, s2, s3)
    print(f"Is s3 formed by interleaving s1 and s2? {result}")
