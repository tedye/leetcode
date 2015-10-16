# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        p = ListNode(-1)
        p.next = head
        temp = head
        i = 0
        flag = False
        while i < n-1:
            if temp:
                temp = temp.next
            else:
                flag = True
                break
            i += 1
        if flag:
            return head
        t = p
        while temp.next:
            temp = temp.next
            t = t.next
        t.next = t.next.next
        return p.next
        
            
        