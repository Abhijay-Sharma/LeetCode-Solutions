class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element=nums[0]
        count=0
        length=len(nums)
        for i in range(length):
            if nums[i]==element:
                count+=1
            else:
                count-=1
            if count==0:
                element=nums[i+1]
        count=0
        for j in nums:
            if j==element:
                count+=1
        if count>length/2:
            return element
