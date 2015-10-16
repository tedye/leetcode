class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        l = len(nums)
        k %= l
        gcd = self.GCD(l,k)
        for i in range(gcd):
            cur = i
            temp = nums[i]
            while 1:
                next = (cur+k) % l
                if next == i: break
                temp1 = nums[next]
                nums[next] = temp 
                cur = next
                temp = temp1
            nums[i] = temp
        
    
    def GCD(self,a,b):
        if a == 0: return b
        return self.GCD(b%a,a)
        