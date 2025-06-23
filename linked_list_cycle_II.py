class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def detectCycle(self, head):
        slow = fast = head

        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle

        # Step 2: Find the start node of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

# 🔧 Helper to build linked list with cycle at given position
def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

# 🧪 Test Case
if __name__ == "__main__":
    # 📥 Input
    head_values = [3, 2, 0, -4]
    pos = 1  # Tail connects to index 1
    head = create_linked_list_with_cycle(head_values, pos)

    # 🔍 Solution
    sol = Solution()
    cycle_node = sol.detectCycle(head)

    # 🖨️ Output
    if cycle_node:
        print(f"Output: tail connects to node index {pos}")
        print(f"Explanation: There is a cycle in the linked list, where tail connects to the node with value = {cycle_node.val}.")
    else:
        print("Output: no cycle")
