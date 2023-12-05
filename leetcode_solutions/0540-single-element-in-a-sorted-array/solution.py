class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        start=0
        end=length-1
        # Edge cases:
        if length == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[length - 1] != nums[length - 2]:
            return nums[length - 1]
        while start <= end:
            mid=(start+end)//2
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
                return nums[mid]
            if nums[mid]==nums[mid+1]:
                if (end-mid-1)%2!=0:
                    start=mid+2
                else:
                    end=mid-1
            if nums[mid]==nums[mid-1]:
                if (mid-start-1)%2!=0:
                    end=mid-2
                else:
                    start=mid+1
