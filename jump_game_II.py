class Solution:
    def jump(self, nums):
        n = len(nums)
        jumps = 0       # Number of jumps taken
        farthest = 0    # Farthest index we can currently reach
        end = 0         # End of current jump range

        for i in range(n - 1):  # we don't need to check last index
            farthest = max(farthest, i + nums[i])  # update farthest reach

            # if we reach the end of current range, take a jump
            if i == end:
                jumps += 1
                end = farthest   # move the range boundary

        return jumps
