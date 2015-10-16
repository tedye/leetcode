# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head:
            return head
        l = []
        temp = head
        while temp:
            l.append(temp)
            temp = temp.next
        l.sort(key = lambda x: x.val)
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        l[-1].next= None
        return l[0]