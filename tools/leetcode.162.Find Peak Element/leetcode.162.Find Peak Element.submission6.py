class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 0: return None
        if len(num) == 1: return 0
        return self.findPeakElementHelper(num,0,len(num)-1,len(num))
        
    def findPeakElementHelper(self, arr, start, end, length):
        mid = start + (end - start) // 2
        
        if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == length-1 or arr[mid+1] <= arr[mid]): return mid
        elif mid > 0 and arr[mid-1] > arr[mid]:
            return self.findPeakElementHelper(arr,start,mid-1,length)
        else: return self.findPeakElementHelper(arr,mid+1,end,length)