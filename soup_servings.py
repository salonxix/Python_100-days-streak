def soupServings(n: int) -> float:
    # Scaling down to units of 25 mL
    if n > 4800:  # For large n, probability approaches 1
        return 1.0

    n = (n + 24) // 25  # Convert to 25 mL units

    from functools import lru_cache

    @lru_cache(None)
    def dp(a, b):
        # Base cases
        if a <= 0 and b <= 0:
            return 0.5  # Both empty at the same time
        if a <= 0:
            return 1.0  # A empty first
        if b <= 0:
            return 0.0  # B empty first

        # Four operations each with probability 0.25
        return 0.25 * (
            dp(a - 4, b) +         # 100mL from A, 0mL from B
            dp(a - 3, b - 1) +     # 75mL from A, 25mL from B
            dp(a - 2, b - 2) +     # 50mL from A, 50mL from B
            dp(a - 1, b - 3)       # 25mL from A, 75mL from B
        )

    return dp(n, n)


# Example usage
print(soupServings(50))   # 0.62500
print(soupServings(100))  # 0.71875
