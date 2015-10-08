# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        depth = 0
        temp = head
        while temp:
            temp = temp.next
            depth += 1
        if depth & 1:
            l = depth // 2
        else:
            l = depth // 2 - 1
        x = head
        i = 0
        while i < l:
            x = x.next
            i += 1
        
        l2 = self.reverseList(x.next)
        x.next = None
        l1 = head
        

        dummy = ListNode(0)
        temp = dummy
        while l1 or l2:
            temp1 = l1
            l1 = l1.next
            temp1.next = None
            temp.next = temp1
            temp = temp.next
            if l2:
                temp2 = l2
                l2 = l2.next
                temp2.next = None
                temp.next = temp2
                temp = temp.next
    
    def reverseList(self,node):
        if not node:
            return None
        wkset = [None, node, node.next]
        while wkset[1]:
            wkset[1].next = wkset[0]
            wkset[0] = wkset[1]
            wkset[1] = wkset[2]
            if wkset[2]:
                wkset[2]=  wkset[2].next
        return wkset[0]  