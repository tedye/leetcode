# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if not head: return None
        if k == 1: return head
        if head.next == None: return head
        
        [h,t,n] = self.travel(head,k)
        if n == None:
            return h
        temp = t
        next = n
        while next != None:
            [he,ta,ne] = self.travel(next,k)
            temp.next = he
            temp = ta
            next = ne

        return h
            
    
    def travel(self,head,k):
        cnt = 1
        temp = head
        while cnt < k and temp != None:
            temp = temp.next
            cnt += 1
        if temp == None:
            return head,temp,None
        next = temp.next
        temp1 = head
        temp2 = temp1.next
        temp1.next = None
        while temp2 != temp:
            x = temp2.next
            temp2.next = temp1
            temp1 = temp2
            temp2 = x
        temp.next = temp1
        head.next = next
        return temp, head, next

    def printNode(self,head):
        while head != None:
            print(head.val)
            head = head.next
        