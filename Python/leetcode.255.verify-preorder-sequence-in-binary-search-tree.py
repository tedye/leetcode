class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        '''
        # first attempt: mimic reconstruct 
        # BST from preorder and inorder sequence
        inorder = sorted(preorder)
        n = len(preorder)
        return self.helper(preorder,0, n-1, inorder, 0, n-1)
    
    def helper(self, preorder, pres, pree, inorder, ins, ine):
        '''
        # This function is used to detect with given 
        # preorder and inorder sequence can be used to 
        # construct a valid BST in recursive way
        # Input: two list[int]
        # Output: bool
        '''
        lengthPre = pree - pres + 1
        lengthIn = ine - ins + 1
        if lengthPre != lengthIn or set(preorder[pres:pree+1])-set(inorder[ins:ine+1]):
            return False
        if lengthPre < 2:
            return preorder[pres:pree+1] == inorder[ins:ine+1]
        
        rootnode = preorder[pres]
        try:
            ind = inorder[ins:ine+1].index(rootnode)
        except ValueError:
            return False
        return self.helper(preorder,pres+1,pres+ind,inorder,ins,ins+ind-1) and self.helper(preorder,pres+ind+1,pree,inorder,ins+ind+1,ine)
        # failed to pass the large testing case
        '''
        
        # use path to keep parent for right child
        low = -0x7fffffff
        path = []
        for p in preorder:
            if p < low:
                return False
            while path and p > path[-1]:
                low = path[-1]
                path.pop()
            path.append(p)
        return True
        
            