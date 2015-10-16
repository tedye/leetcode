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
        dummy = ListNode(0)
        temp = dummy
        while l1 or l2 or carry:
            op1 = op2 = 0
            if l1 and l2:
                op1 = l1.val
                op2 = l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                op1 = l1.val
                l1 = l1.next
            elif l2:
                op2 = l2.val
                l2 = l2.next
            s = op1 + op2 + carry
            temp.next = ListNode(s%10)
            carry = s//10
            temp = temp.next
        return dummy.next