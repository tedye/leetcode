# Definition for singly-linked list.# class ListNode:#     def __init__(self, x):#         self.val = x#         self.next = Noneclass Solution:    # @param a list of ListNode    # @return a ListNode    def mergeKLists(self, lists):        if not lists: return None        if len(lists) == 1: return lists[0]                l = [(a.val,a) for a in lists if a]        l.sort()        res = ListNode(-0x7fffffff)        temp = res        while l:            a = l[0]            l.remove(a)            b = a[1].next            a[1].next = None            temp.next = a[1]            if b:                l.append((b.val,b))                l.sort()            temp = temp.next        return res.next            