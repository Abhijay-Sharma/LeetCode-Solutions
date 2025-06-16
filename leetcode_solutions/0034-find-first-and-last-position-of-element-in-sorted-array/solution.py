class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        first_occurence,last_occurence=-1,-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid - 1
                if nums[mid] == target:
                    first_occurence = mid
            else:
                start = mid + 1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
                if nums[mid] == target:
                    last_occurence = mid
            else:
                end = mid - 1

        return (first_occurence,last_occurence)
