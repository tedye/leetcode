# Definition for singly-linked list.# class ListNode:#     def __init__(self, x):#         self.val = x#         self.next = Noneclass Solution:    # @param head, a ListNode    # @return a list node    def detectCycle(self, head):        s = set()        if not head:            return None                temp = head        while temp:            if temp not in s:                s.add(temp)            else:                return temp            temp = temp.next        return None        