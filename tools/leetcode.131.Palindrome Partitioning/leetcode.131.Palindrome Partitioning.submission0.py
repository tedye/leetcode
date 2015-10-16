class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
            
        current = []
        result = []
        self.helper(s, current, result)
        return result
    
    def helper(self, s, cur, res):
        if not s:
            if cur:
                res.append(cur[:])
            return
        
        for i in range(1,len(s)+1):
            if s[:i] == s[:i][::-1]:
                cur.append(s[:i])
                self.helper(s[i:], cur, res)
                cur.pop(-1)