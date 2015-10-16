class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dic = {}
        length = len(num)
        for number in num:
            if number not in dic.keys():
                dic[number] = 1
            else: dic[number] += 1
            
            if dic[number] * 2 >= length:
                return number