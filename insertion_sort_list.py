# insertion_sort_list.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(0)  # Dummy head for the sorted list
        current = head

        while current:
            prev = dummy
            next_temp = current.next

            # Find the correct position in sorted part
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current node in sorted list
            current.next = prev.next
            prev.next = current

            # Move to the next node in original list
            current = next_temp

        return dummy.next

# 🔧 Helper function to create linked list from list
def create_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# 🔧 Helper function to convert linked list to list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# 🧪 Test Case
if __name__ == "__main__":
    input_list = [4, 2, 1, 3]
    head = create_linked_list(input_list)

    sol = Solution()
    sorted_head = sol.insertionSortList(head)

    print("Output:", print_linked_list(sorted_head))  # Output: [1, 2, 3, 4]
