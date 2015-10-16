# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if not head: return None
        if m == n: return head
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        chain = []
        c = 1
        while c < m:
            temp = temp.next
            c += 1
        parent = temp
        temp = parent.next
        while c <= n:
            chain.append(temp)
            temp = temp.next
            c += 1
        tail = temp
        
        chain = chain[::-1]
        for i in range(len(chain)-1):
            chain[i].next = chain[i+1]
        
        parent.next = chain[0]
        chain[-1].next = tail
        
        return dummy.next
        
        
        
            
        