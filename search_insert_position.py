from typing import List

def search_insert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Example usage
if __name__ == "__main__":
    try:
        nums = list(map(int, input("Enter sorted array (space-separated): ").split()))
        target = int(input("Enter target value: "))
        index = search_insert(nums, target)
        print(f"Target would be inserted at index: {index}")
    except ValueError:
        print("Invalid input. Please enter integers only.")
