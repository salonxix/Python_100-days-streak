# reorder_list.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: Find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow.next
        slow.next = None  # Break the list into two
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

# 🔧 Helper to create and print linked list
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print("Output:", result)

# 🧪 Test
if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4])
    Solution().reorderList(head)
    print_linked_list(head)  # Output: [1, 4, 2, 3]
