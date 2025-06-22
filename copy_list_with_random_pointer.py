# copy_random_list_runner.py

class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # Step 1: Interweave copied nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        # Step 2: Set random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate original and copied list
        original = head
        copy_head = head.next
        copy = copy_head
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next

        return copy_head

# Helper to build linked list from input format [[val, random_index], ...]
def build_linked_list(data):
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]
    for i, (_, rand_i) in enumerate(data):
        if i < len(data) - 1:
            nodes[i].next = nodes[i + 1]
        nodes[i].random = nodes[rand_i] if rand_i is not None else None
    return nodes[0]

# Helper to convert linked list to [[val, random_index], ...]
def linked_list_to_array(head):
    index_map = {}
    result = []
    curr = head
    i = 0
    while curr:
        index_map[curr] = i
        curr = curr.next
        i += 1
    curr = head
    while curr:
        rand_index = index_map[curr.random] if curr.random else None
        result.append([curr.val, rand_index])
        curr = curr.next
    return result

# 🔧 Test Example
if __name__ == "__main__":
    # Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
    data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = build_linked_list(data)

    sol = Solution()
    copied_head = sol.copyRandomList(head)

    output = linked_list_to_array(copied_head)
   
    print(output)
