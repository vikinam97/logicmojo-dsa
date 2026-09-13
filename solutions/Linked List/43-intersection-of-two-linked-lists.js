# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1, c2 = 0, 0
        node = headA
        while node:
            c1 += 1
            node = node.next
        node = headB
        while node:
            c2 += 1
            node = node.next
        
        while c2 > c1:
            headB = headB.next
            c2 -= 1 
        
        while c1 > c2:
            headA = headA.next
            c1 -= 1 
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA