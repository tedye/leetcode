class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.d1 = collections.defaultdict(int) # contains added nums

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.d1[number] += 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for n in self.d1:
            if value - n in self.d1 and (value - n != n or self.d1[n] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)