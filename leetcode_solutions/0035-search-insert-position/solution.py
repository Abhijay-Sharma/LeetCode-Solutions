class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        ans= end+1      #its acrtually len just doing this for better complx..
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                ans=mid
                end = mid - 1
            else:
                start = mid + 1
        return ans
        
