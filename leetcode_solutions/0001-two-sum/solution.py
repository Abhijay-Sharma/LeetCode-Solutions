class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary={}
        for i in range(len(nums)):
            if target - nums[i] in dictionary:
                return [dictionary[target-nums[i]],i]
            else:
                dictionary[nums[i]]=i
            
