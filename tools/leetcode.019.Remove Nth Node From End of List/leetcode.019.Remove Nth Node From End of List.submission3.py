# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        parent = head
        toRemove = head
        temp = head
        for i in range(n-1):
            temp = temp.next
        if temp.next == None:
            return head.next
        else: 
            temp = temp.next
            toRemove = toRemove.next
        while temp.next != None:
            temp = temp.next
            toRemove = toRemove.next
            parent = parent.next
        parent.next = toRemove.next
        return head
        