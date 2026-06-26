# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head2):
            p, c = None, head2
            while c:
                n = c.next
                c.next = p
                p = c
                c = n
            return p

        s, f = head, head
        while s and f and f.next and f.next.next:
            s = s.next
            f = f.next.next
        
        head2 = s.next
        s.next = None

        head2 = reverse(head2)

        node = head
        while node and head2:
            t = head2.next

            head2.next = node.next
            node.next = head2

            node = head2.next
            head2 = t

        return head
        