class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        # Build the segment tree
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, val):
        pos = index + self.n
        self.tree[pos] = val
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]

    def sumRange(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left <= right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 0:
                result += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return result


# ----------- DRIVER CODE (for testing) ------------
if __name__ == "__main__":
    numArray = NumArray([1, 3, 5])
    print(numArray.sumRange(0, 2))  # Output: 9
    numArray.update(1, 2)
    print(numArray.sumRange(0, 2))  # Output: 8
