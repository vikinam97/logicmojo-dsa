class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, c = None, head
        while c:
            n = c.next
            c.next = p
            p = c
            c = n
        return p