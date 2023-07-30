class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left , right =0 , 0             #pointers
        length=len(nums)
        maxsum=nums[0]
        currentsum=0
        for i in nums:
            if i > maxsum:
                maxsum=i
        while right < length:
            if nums[left]>0:
                currentsum+=nums[right]
                if currentsum<0:
                    left=right
                if currentsum>maxsum:
                    maxsum=currentsum
                right+=1
            else:
                left+=1
                right=left
                currentsum=0
        return maxsum
