# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        temp = head
        while temp.next!= None:
            temp.val = 0x7fffffff
            temp = temp.next
            if temp.val == 0x7fffffff:
                return True
        return False