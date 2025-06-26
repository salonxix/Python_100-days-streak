class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

# 🔧 Helper to build intersecting linked lists
def build_lists(intersect_val, listA_vals, listB_vals, skipA, skipB):
    def build_nodes(vals):
        head = ListNode(vals[0])
        curr = head
        nodes = [head]
        for val in vals[1:]:
            curr.next = ListNode(val)
            curr = curr.next
            nodes.append(curr)
        return head, nodes

    headA, nodesA = build_nodes(listA_vals)
    headB, nodesB = build_nodes(listB_vals)

    if intersect_val:
        intersect_node = nodesA[skipA]
        nodesB[skipB - 1].next = intersect_node

    return headA, headB

# ✅ Test Example
if __name__ == "__main__":
    headA, headB = build_lists(
        intersect_val=8,
        listA_vals=[4, 1, 8, 4, 5],
        listB_vals=[5, 6, 1],
        skipA=2,
        skipB=3
    )
    result = getIntersectionNode(headA, headB)
    print("Intersected at node with value:", result.val if result else "No intersection")
