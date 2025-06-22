# linked_list_cycle.py

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# 🔧 Helper to build linked list with cycle at position `pos`
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]  # Create cycle
    return nodes[0]

# 🧪 Test
if __name__ == "__main__":
    sol = Solution()

    # Example: [3,2,0,-4], pos = 1
    head = create_linked_list_with_cycle([3, 2, 0, -4], 1)
    print("Cycle exists:", sol.hasCycle(head))  # Output: True

    # Example: [1,2], pos = -1 (no cycle)
    head2 = create_linked_list_with_cycle([1, 2], -1)
    print("Cycle exists:", sol.hasCycle(head2))  # Output: False
