# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(-1)
        temp = dummy
        while carry or l1 or l2:
            op1 = op2 = 0
            if l1:
                op1 = l1.val
                l1 = l1.next
            if l2:
                op2 = l2.val
                l2 = l2.next
            s = op1+op2+carry
            carry = s//10
            s %=10
            temp.next = ListNode(s)
            temp = temp.next
            
        return dummy.next
        