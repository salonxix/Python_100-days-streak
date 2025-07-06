def max_active_sections(s: str) -> int:
    t = '1' + s + '1'
    n = len(t)
    initial_ones = t.count('1')

    remove_blocks = []  # (start, end, size)
    gain_blocks = []    # (start, end, size)

    i = 0
    while i < n:
        if t[i] == '1':
            j = i
            while j < n and t[j] == '1':
                j += 1
            if i > 0 and j < n and t[i - 1] == '0' and t[j] == '0':
                remove_blocks.append((i, j - 1, j - i))
            i = j
        elif t[i] == '0':
            j = i
            while j < n and t[j] == '0':
                j += 1
            if i > 0 and j < n and t[i - 1] == '1' and t[j] == '1':
                gain_blocks.append((i, j - 1, j - i))
            i = j
        else:
            i += 1

    max_active = initial_ones

    for _, _, r_size in remove_blocks:
        for _, _, g_size in gain_blocks:
            max_active = max(max_active, initial_ones - r_size + g_size)

    return max_active

# 🔍 Test Cases
print(max_active_sections("01"))       # ➞ 1
print(max_active_sections("0100"))     # ➞ 4
print(max_active_sections("1000100"))  # ➞ 7
print(max_active_sections("01010"))    # ➞ 4
