from collections import Counter, defaultdict

def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    need = Counter(t)
    window = defaultdict(int)
    
    have = 0
    need_count = len(need)
    res = [-1, -1]
    res_len = float('inf')
    
    left = 0
    for right in range(len(s)):
        char = s[right]
        window[char] += 1

        if char in need and window[char] == need[char]:
            have += 1

        while have == need_count:
            # Update result
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1
            
            # Pop from left
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1
    
    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""



if __name__ == "__main__":
    s1, t1 = "ADOBECODEBANC", "ABC"
    print("Test Case 1 Output:", minWindow(s1, t1))  # Expected: "BANC"

    s2, t2 = "a", "a"
    print("Test Case 2 Output:", minWindow(s2, t2))  # Expected: "a"

    s3, t3 = "a", "aa"
    print("Test Case 3 Output:", minWindow(s3, t3))  # Expected: ""
