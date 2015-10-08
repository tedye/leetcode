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
        if not head:
            return None
        
        temp = head
        cur = temp.val
        while temp.next:
            if temp.next.val == cur:
                temp.next = temp.next.next
            else:
                temp = temp.next
                cur = temp.val
        return head