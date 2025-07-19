class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def getDecimalValue(head):
    num = 0
    while head:
        num = (num << 1) | head.val
        head = head.next
    return num

# Test Case 1
head1 = build_linked_list([1, 0, 1])
print("Binary: [1, 0, 1] -> Decimal:", getDecimalValue(head1))  # Output: 5

# Test Case 2
head2 = build_linked_list([0])
print("Binary: [0] -> Decimal:", getDecimalValue(head2))  # Output: 0

# Test Case 3
head3 = build_linked_list([1, 1, 1, 1])
print("Binary: [1, 1, 1, 1] -> Decimal:", getDecimalValue(head3))  # Output: 15
