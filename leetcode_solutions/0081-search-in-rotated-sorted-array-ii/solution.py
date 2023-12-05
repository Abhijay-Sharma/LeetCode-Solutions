class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        length=len(nums)
        start=0
        end=length-1
        while start <= end and start<length and end<length:
            mid=(start+end)//2
            if nums[mid]==target:
                return True
            #Edge case
            if nums[start]==nums[mid] and nums[mid] == nums [end]:
                start+=1
                end-=1
                continue
            #If left part is sorted
            if nums[start]<=nums[mid]:
                if nums[start]<= target<=nums[mid]:#element exists here
                    end=mid-1
                else:
                    start=mid+1
            # If right part is sorted
            elif nums[mid]<=nums[end]:
                if  nums[mid]<=target<=nums[end]: #element exists here
                    start=mid+1
                else:
                    end=mid-1
        return False
