from __future__ import annotations
import copy


class ListNode:
    def __init__(self, value: int, next: ListNode=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        curr = self
        res = []

        while curr:
            res.append(curr.value)
            curr = curr.next
        
        return str(res)
    
    def pop_last_node(self) -> ListNode:
        temp = self
        while temp.next:
            prev = temp
            temp = temp.next

        ret = prev.next
        prev.next = None
        return ret

    def reversed(self) -> ListNode:
        lst = copy.deepcopy(self)
        lst = ListNode.reverse(lst)
        return lst

    @staticmethod
    def reverse(lst: ListNode) -> ListNode:
        if lst is None or lst.next is None:
            return lst
            
        value = lst.pop_last_node().value

        return ListNode(value, ListNode.reverse(lst))


if __name__ == "__main__":
    linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    ll_reversed = linked_list.reversed()
    print(ll_reversed, linked_list)