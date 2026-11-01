# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        res = ListNode()
        curres = res
        carry = 0
        first = True
        while True:
            if cur1 is None and cur2 is None and carry == 0:
                break
            newVal = 0
            if cur1 is not None:
                newVal += cur1.val
                cur1 = cur1.next
            if cur2 is not None:
                newVal += cur2.val
                cur2 = cur2.next
            newVal += carry
            print (newVal)
            
            if not first:
                curres.next = ListNode()
                curres = curres.next
            else:
                first = False
            curres.val = newVal % 10
            carry = newVal // 10
            
        
        return res
        