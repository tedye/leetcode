# Definition for singly-linked list.# class ListNode:#     def __init__(self, x):#         self.val = x#         self.next = Noneclass Solution:    # @param head, a ListNode    # @return a list node    def detectCycle(self, head):        if head == None:            return None        temp = head        while temp.next != None:            temp.val = 0x7fffffff            temp = temp.next             if temp.val == 0x7fffffff:                return temp        return None