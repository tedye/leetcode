# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head or not head.next or k == 1 or k == 0: return head
        dummy = ListNode(0)
        dummy.next = head
        parent = dummy
        while parent:
            l = [None] *(k+2)
            i = 0
            temp = parent
            while i < k+2 and temp:
                l[i] = temp
                temp = temp.next
                i+=1
            if l.count(None) > 1:
                break
            l[1:k+1] = l[1:k+1][::-1]
            for i in range(k+1):
                l[i].next = l[i+1]
            parent = l[-2]
        return dummy.next
                
        
        