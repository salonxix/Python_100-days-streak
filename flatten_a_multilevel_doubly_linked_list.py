class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        stack = []
        curr = head

        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)

                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None

            if not curr.next and stack:
                curr.next = stack.pop()
                curr.next.prev = curr

            curr = curr.next

        return head

# Helper to print flattened list
def print_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    print(result)

# Helper to manually build multilevel list from example
def build_sample_list():
    # Level 1
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    # Level 2
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)

    # Level 3
    n11 = Node(11)
    n12 = Node(12)

    # Connect Level 1
    n1.next = n2; n2.prev = n1
    n2.next = n3; n3.prev = n2
    n3.next = n4; n4.prev = n3
    n4.next = n5; n5.prev = n4
    n5.next = n6; n6.prev = n5

    # Connect child of 3 to 7
    n3.child = n7

    # Connect Level 2
    n7.next = n8; n8.prev = n7
    n8.next = n9; n9.prev = n8
    n9.next = n10; n10.prev = n9

    # Connect child of 8 to 11
    n8.child = n11

    # Connect Level 3
    n11.next = n12; n12.prev = n11

    return n1

# Main execution
if __name__ == "__main__":
    head = build_sample_list()
    sol = Solution()
    flat_head = sol.flatten(head)
    print_list(flat_head)
