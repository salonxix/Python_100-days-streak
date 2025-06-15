class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head):
    # Base case
    if not head:
        return None
    if not head.next:
        return TreeNode(head.val)

    # Find middle of linked list (slow-fast pointers)
    prev = None
    slow = fast = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Disconnect left part from mid
    if prev:
        prev.next = None

    root = TreeNode(slow.val)
    root.left = sortedListToBST(head if prev else None)
    root.right = sortedListToBST(slow.next)

    return root

# Helper to convert list to linked list
def createLinkedList(nums):
    dummy = ListNode(0)
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next

# Helper to print level order for verification
from collections import deque
def levelOrderTraversal(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val if node else None)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        if any(x is not None for x in level):
            result.append(level)
    return result

# -------------------- Run --------------------

nums = [-10, -3, 0, 5, 9]
linked_list = createLinkedList(nums)
tree = sortedListToBST(linked_list)

print("Input: head =", nums)
print("Output (Level Order):", levelOrderTraversal(tree))
