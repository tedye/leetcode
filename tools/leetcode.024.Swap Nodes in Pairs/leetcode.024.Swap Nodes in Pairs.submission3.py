# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None: return head
        if head.next == None: return head
        
        temp = ListNode(-1) #dummy head
        temp.next = head
        temp0 = temp
        temp1 = head
        temp2 = head.next
        while temp1 != None and temp2 != None:
            temp3 = temp2.next
            temp0.next = temp2
            temp2.next = temp1
            temp1.next = temp3
            temp0 = temp1
            temp1 = temp0.next
            if temp1 != None:
                temp2 = temp1.next
        return temp.next