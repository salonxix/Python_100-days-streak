class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2
    return dummy.next

# Utility to convert list to linked list (for testing)
def list_to_linkedlist(elements):
    dummy = ListNode()
    current = dummy
    for el in elements:
        current.next = ListNode(el)
        current = current.next
    return dummy.next

# Utility to convert linked list to list (for output)
def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage:
list1 = list_to_linkedlist([1, 2, 4])
list2 = list_to_linkedlist([1, 3, 4])
merged_head = mergeTwoLists(list1, list2)
print(linkedlist_to_list(merged_head))  # Output: [1, 1, 2, 3, 4, 4]
