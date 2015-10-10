# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        if length == 0:
            return True
        if length == 1:
            return True
        if length == 2:
            return head.val == head.next.val
        if length == 3:
            return head.val == head.next.next.val
            
        temp = head
        half = length // 2
        while half > 0:
            half -= 1
            temp = temp.next
        if length%1:
            temp = temp.next
        workset = [temp, temp.next, temp.next.next]
        temp.next = None
        while workset[1]:
            workset[1].next = workset[0]
            workset[0] = workset[1]
            workset[1] = workset[2]
            if workset[2]:
                workset[2] = workset[2].next
        temp = workset[0]
        temp1 = head
        while temp and temp1:
            if temp.val != temp1.val:
                return False
            temp = temp.next
            temp1 = temp1.next
        return True