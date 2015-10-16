# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None: return None
        temp = []
        while head != None:
            temp.append(head.val)
            head = head.next
        temp = sorted(list(set(temp)))
        temp = [ListNode(i) for i in temp]
        temp.append(None)
        temp = temp[::-1]
        for i in range(1,len(temp)):
            temp[i].next = temp[i-1] 
        return temp[-1]