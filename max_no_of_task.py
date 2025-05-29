from typing import List
import heapq

def maxTaskAssign(tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
    """
    Find the maximum number of tasks that can be completed.
    
    Args:
        tasks: List of task strength requirements
        workers: List of worker strengths
        pills: Number of magical pills available
        strength: Strength boost per pill
        
    Returns:
        Maximum number of tasks that can be completed
    """
    def canComplete(k: int) -> bool:
        """Check if we can complete k easiest tasks"""
        if k == 0:
            return True
            
        # Take k easiest tasks and all workers
        selected_tasks = sorted(tasks)[:k]
        available_workers = workers[:]
        pills_used = 0
        
        # Try to assign tasks greedily (hardest first)
        for task in reversed(selected_tasks):
            assigned = False
            
            # First try to assign without pill (strongest worker first)
            for i in range(len(available_workers) - 1, -1, -1):
                if available_workers[i] >= task:
                    available_workers.pop(i)
                    assigned = True
                    break
            
            if assigned:
                continue
                
            # Need to use a pill - find weakest worker who can do it with pill
            if pills_used < pills:
                for i in range(len(available_workers)):
                    if available_workers[i] + strength >= task:
                        available_workers.pop(i)
                        pills_used += 1
                        assigned = True
                        break
            
            if not assigned:
                return False
                
        return True
    
    # Binary search on number of tasks
    left, right = 0, min(len(tasks), len(workers))
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if canComplete(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

# Test cases
def test_solution():
    # Example 1
    tasks1 = [3,2,1]
    workers1 = [0,3,3]
    pills1 = 1
    strength1 = 1
    print(f"Input: tasks={tasks1}, workers={workers1}, pills={pills1}, strength={strength1}")
    print(f"Output: {maxTaskAssign(tasks1, workers1, pills1, strength1)}")  # Expected: 3
    print()

if __name__ == "__main__":
    test_solution()
