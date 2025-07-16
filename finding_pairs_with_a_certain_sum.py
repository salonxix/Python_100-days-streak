from collections import Counter

class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = Counter(nums2)

    def add(self, index, val):
        old_val = self.nums2[index]
        self.freq2[old_val] -= 1
        self.nums2[index] += val
        new_val = self.nums2[index]
        self.freq2[new_val] += 1

    def count(self, tot):
        count = 0
        for num in self.nums1:
            count += self.freq2.get(tot - num, 0)
        return count

# ---------- Testing the class in terminal ----------

findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])

print(findSumPairs.count(7))  # Output: 8
findSumPairs.add(3, 2)        # nums2[3] becomes 4
print(findSumPairs.count(8))  # Output: 2
print(findSumPairs.count(4))  # Output: 1
findSumPairs.add(0, 1)        # nums2[0] becomes 2
findSumPairs.add(1, 1)        # nums2[1] becomes 5
print(findSumPairs.count(7))  # Output: 11
