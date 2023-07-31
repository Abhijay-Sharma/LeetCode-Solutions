class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length=len(nums)
        rearranged=["*"]*length
        even,odd=0,1
        for number in nums:
            if number>0:
                rearranged[even]=number
                even+=2
            else:
                rearranged[odd]=number
                odd+=2
        return rearranged
