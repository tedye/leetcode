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
        
        dummyHead = ListNode(-0x7fffffff)
        dummyHead.next = head
        
        temp = dummyHead
        temp1 = temp.next
        temp2 = temp1

        while temp2.next != None:
            temp2 = temp2.next
            while temp2 != None and temp2.val == temp1.val:
                temp2 = temp2.next
                if temp2 != None and temp2.val != temp1.val:
                    temp1 = temp2
                    temp2 = temp2.next
            if temp2 == None:
                if temp1.next == temp2:
                    temp.next = temp1
                else:
                    temp.next = None
                break
            temp.next = temp1
            temp = temp.next
            temp1 = temp.next
            temp2 = temp1            
        return dummyHead.next
                