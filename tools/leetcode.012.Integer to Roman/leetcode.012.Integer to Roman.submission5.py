class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        map000 = ['','M','MM','MMM']
        map00 = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        map0 = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        map = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        res = ''
        res += map000[num // 1000]
        num %= 1000
        res += map00[num // 100]
        num %= 100
        res += map0[num // 10]
        num %= 10
        res += map[num]
        return res
        