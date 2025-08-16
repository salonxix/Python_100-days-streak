class MapSum:

    def __init__(self):
        self.map = {}  # stores key → value mapping

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val  # insert/override key

    def sum(self, prefix: str) -> int:
        total = 0
        for k, v in self.map.items():
            if k.startswith(prefix):
                total += v
        return total


# ---- Test Example (like problem statement) ----
if __name__ == "__main__":
    mapSum = MapSum()
    mapSum.insert("apple", 3)
    print(mapSum.sum("ap"))   # Expected 3

    mapSum.insert("app", 2)
    print(mapSum.sum("ap"))   # Expected 5
