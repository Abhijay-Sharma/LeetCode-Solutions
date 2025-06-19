class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start,end=0,len(nums)-1

        while start<end:
            mid=(start+end)//2

            #first step is to identify odd and even halves

            if mid%2==1:
                mid-=1

            if nums[mid]==nums[mid+1]:
                start+=2
            else:
                end=mid

        return nums[start]
