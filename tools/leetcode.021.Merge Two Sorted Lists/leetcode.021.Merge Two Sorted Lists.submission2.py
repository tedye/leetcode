# Definition for singly-linked list.# class ListNode:#     def __init__(self, x):#         self.val = x#         self.next = Noneclass Solution:    # @param {ListNode} l1    # @param {ListNode} l2    # @return {ListNode}    def mergeTwoLists(self, l1, l2):        dummy = ListNode(None)        temp1 = l1        temp2 = l2        temp3 = dummy        while temp1 and temp2:            if temp1.val < temp2.val:                temp3.next = temp1                temp1 = temp1.next                temp3 = temp3.next            else:                temp3.next = temp2                temp2 = temp2.next                temp3 = temp3.next        if temp1:            temp3.next = temp1        if temp2:            temp3.next = temp2        return dummy.next        