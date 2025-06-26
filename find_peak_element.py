from typing import List

def findPeakElement(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            # Peak lies to the left (or at mid)
            right = mid
        else:
            # Peak lies to the right
            left = mid + 1

    return left  # or right, since left == right

# ✅ Test Examples
if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 1, 3, 5, 6, 4]
    print("Peak index in nums1:", findPeakElement(nums1))  # ➤ 2
    print("Peak index in nums2:", findPeakElement(nums2))  # ➤ 5 or 1 (both valid)
