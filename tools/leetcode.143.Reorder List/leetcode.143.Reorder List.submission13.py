# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None: return None
        if head.next == None: return head
        if head.next.next == None: return head
        
        a = []
        temp = head
        while temp != None:
            a.append(temp)
            temp = temp.next

        l = len(a) - 1
        s = 0
        b = []
        while s <= l:
            b.append(a[s])
            s += 1
            if l > s:
                b.append(a[l])
                l -= 1
        
        b.append(None)
        
        for i in range(len(a)):
            b[i].next = b[i+1]
            

        
            
        
        