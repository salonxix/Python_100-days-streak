def removeSubfolders(folder):
    folder.sort()
    res = []
    
    for f in folder:
        if not res or not f.startswith(res[-1] + "/"):
            res.append(f)
    
    return res

# 🔧 Example tests
print(removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))  # Output: ["/a","/c/d","/c/f"]
print(removeSubfolders(["/a","/a/b/c","/a/b/d"]))              # Output: ["/a"]
print(removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))         # Output: ["/a/b/c","/a/b/ca","/a/b/d"]
