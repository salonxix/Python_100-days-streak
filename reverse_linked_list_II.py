class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node before `left`
    for _ in range(left - 1):
        prev = prev.next

    # Start reversing
    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next

# 🔧 Helper function to create linked list from array
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# 🔧 Helper function to convert linked list to Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# 🧪 Get user input and run the function
arr = list(map(int, input("Enter linked list elements separated by space: ").split()))
left = int(input("Enter left position: "))
right = int(input("Enter right position: "))

head = create_linked_list(arr)
reversed_head = reverseBetween(head, left, right)
print("Reversed Linked List:", linked_list_to_list(reversed_head))
