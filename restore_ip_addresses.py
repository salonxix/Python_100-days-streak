def restoreIpAddresses(s: str):
    res = []

    def backtrack(start=0, path=[]):
        if len(path) == 4:
            if start == len(s):
                res.append(".".join(path))
            return

        for end in range(start + 1, min(start + 4, len(s) + 1)):
            part = s[start:end]
            # Check if part is valid
            if (part.startswith("0") and len(part) > 1) or (int(part) > 255):
                continue
            backtrack(end, path + [part])

    backtrack()
    return res

# Example test cases
print(restoreIpAddresses("25525511135"))  # ["255.255.11.135", "255.255.111.35"]
print(restoreIpAddresses("0000"))         # ["0.0.0.0"]
print(restoreIpAddresses("101023"))       # ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
