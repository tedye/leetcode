# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head:
            return head
        
        d1 = ListNode(-1)
        temp1 = d1
        d2 = ListNode(-1)
        temp2 = d2
        temp = head
        while temp:
            if temp.val  < x:
                temp1.next = temp
                temp = temp.next
                temp1 = temp1.next
                temp1.next = None
            else:
                temp2.next = temp
                temp = temp.next
                temp2 = temp2.next
                temp2.next = None
        temp1.next = d2.next
        return d1.next
                
                
                