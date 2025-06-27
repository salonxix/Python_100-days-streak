def compareVersion(version1: str, version2: str) -> int:
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    
    max_len = max(len(v1_parts), len(v2_parts))
    
    for i in range(max_len):
        v1 = v1_parts[i] if i < len(v1_parts) else 0
        v2 = v2_parts[i] if i < len(v2_parts) else 0
        
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
    
    return 0

# ✅ Test Cases
if __name__ == "__main__":
    print(compareVersion("1.2", "1.10"))      # ➤ -1
    print(compareVersion("1.0.1", "1"))       # ➤ 1
    print(compareVersion("1.01", "1.001"))    # ➤ 0
    print(compareVersion("1.0", "1.0.0"))     # ➤ 0
