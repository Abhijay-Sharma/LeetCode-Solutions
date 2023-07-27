class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xorr=0
        for number in nums:
            xorr ^= number
        return xorr
