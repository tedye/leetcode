# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head: return None
        if head.next == None: return head
        
        cur = head
        n = head
        
        while n != None:
            n = n.next
            while n != None and cur.val == n.val :
                n = n.next
            cur.next = n
            cur = cur.next
        
        return head
            
                