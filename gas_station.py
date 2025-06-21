# gas_station.py

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            curr_tank += gain

            # If we run out of gas, reset starting point
            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        return start_index if total_tank >= 0 else -1


# 🔧 Test
if __name__ == "__main__":
    sol = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print("Starting Gas Station Index:", sol.canCompleteCircuit(gas, cost))  # Output: 3
