class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        root = self
        arr = []

        while root:
            arr.append(root.val)
            root = root.next
        
        return str(arr)


def rotate_right(lst: ListNode, k: int) -> ListNode:
    if lst is None:
        return None
    if lst.next is None:
        return lst
    
    k %= get_length(lst)
    
    for _ in range(k):
        lst = rotate_r(lst)
        
    return lst
    
def rotate_r(lst):
    root = lst
    
    while root.next.next:
        root = root.next

    root.next.next = lst
    l2 = root.next
    root.next = None

    return l2

def get_length(lst: ListNode) -> int:
    l = 0
    copy = lst
    
    while copy.next:
        l += 1
        copy = copy.next
    
    return l+1
        




if __name__ == "__main__":
    lst = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    print(rotate_right(lst, 222223))