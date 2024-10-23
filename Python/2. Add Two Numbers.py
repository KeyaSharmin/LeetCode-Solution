# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        c = 0
        while l1 and l2:
            if l1.val + l2.val +c >= 10:
                tail.next = ListNode(l1.val + l2.val +c-10)
                c = 1
            else:
                tail.next = ListNode(l1.val + l2.val +c)
                c = 0
            l1 = l1.next
            l2 = l2.next
            tail = tail.next
        if l1 != None:
            while l1:
                if l1.val + c >= 10:
                    tail.next = ListNode(l1.val+c-10)
                    c = 1
                else:
                    tail.next = ListNode(l1.val+c)
                    c = 0
                l1 = l1.next
                tail = tail.next
        else:
            while l2:
                if l2.val + c >= 10:
                    tail.next = ListNode(l2.val+c-10)
                    c = 1
                else:
                    tail.next = ListNode(l2.val+c)
                    c = 0
                l2 = l2.next
                tail = tail.next
        if c != 0:
            n = ListNode(c)
            tail.next = n
            
        return dummy.next