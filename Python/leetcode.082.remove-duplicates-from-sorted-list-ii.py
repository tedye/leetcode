# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        d = {}
        temp = head
        while temp:
            if temp.val not in d:
                d[temp.val] = 1
            else:
                d[temp.val] += 1
            temp = temp.next
        dummy = ListNode(0)
        dummy.next = head
        p= dummy
        temp= head
        while temp:
            if d[temp.val] > 1:
                temp = temp.next
            else:
                p.next = temp
                p = p.next
                temp = temp.next
        p.next = None
        return dummy.next