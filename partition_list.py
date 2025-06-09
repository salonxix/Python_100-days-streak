class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to partition the list based on x
def partition(head, x):
    before_head = ListNode(0)  # Dummy node for list < x
    after_head = ListNode(0)   # Dummy node for list >= x

    before = before_head
    after = after_head

    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    after.next = None          # End the list
    before.next = after_head.next  # Connect the two partitions

    return before_head.next

# Utility: Create a linked list from a Python list
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Utility: Convert linked list to Python list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# 🚀 Test Cases
test_cases = [
    {"head": [1, 4, 3, 2, 5, 2], "x": 3, "expected": [1, 2, 2, 4, 3, 5]},
    {"head": [2, 1], "x": 2, "expected": [1, 2]},
    {"head": [1, 2, 3], "x": 4, "expected": [1, 2, 3]},
    {"head": [5, 6, 1, 4, 3], "x": 4, "expected": [1, 3, 5, 6, 4]},
    {"head": [3, 1, 2], "x": 2, "expected": [1, 3, 2]}
]

# Run Test Cases
for i, case in enumerate(test_cases):
    head = create_linked_list(case["head"])
    result_head = partition(head, case["x"])
    result_list = linked_list_to_list(result_head)
    print(f"Test Case {i+1}: Input: {case['head']}, x = {case['x']}")
    print(f"Expected Output: {case['expected']}")
    print(f"Your Output:    {result_list}")
    print("✅ Passed" if result_list == case["expected"] else "❌ Failed", "\n")
