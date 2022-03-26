from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        s = self
        ret = []
        while s:
            ret.append(s.val)
            s = s.next
        return str(ret)


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        result = l1.val
        l1 = l1.next
    else:
        result = l2.val
        l2 = l2.next
        
    return ListNode(result, mergeTwoLists(l1, l2))

def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    nodes = []
    result = curr = ListNode()
    
    for lst in lists:
        while lst:
            nodes.append(lst.val)
            lst = lst.next
    
    for node in sorted(nodes):
        curr.next = ListNode(node)
        curr = curr.next
        
    return result.next


if __name__ == "__main__":
    # TESTS
    l1 = ListNode(1, ListNode(4, ListNode(81)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(3, ListNode(5)))
    l4 = ListNode(2, ListNode(3, ListNode(5)))
    l5 = ListNode(2, ListNode(26, ListNode(73)))
    l6 = ListNode(2, ListNode(3, ListNode(62)))
    l7 = ListNode(6, ListNode(10, ListNode(20)))
    l8 = ListNode(2, ListNode(3, ListNode(51)))
    l9 = ListNode(2, ListNode(3, ListNode(12)))
    l10 = ListNode(3, ListNode(10, ListNode(20)))
    l11 = ListNode(2, ListNode(3, ListNode(5)))
    l12 = ListNode(2, ListNode(3, ListNode(66)))
    l13 = ListNode(5, ListNode(6, ListNode(6)))
    
    print(mergeTwoLists(l1, l2))
    print(mergeKLists([l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13]))