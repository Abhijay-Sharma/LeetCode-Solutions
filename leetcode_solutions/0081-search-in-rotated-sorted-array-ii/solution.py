class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start,end=0,len(nums)-1

        while start<=end:
            mid=(start+end)//2
            print(start,mid,end)
            if nums[mid]==target:
                return True
            if nums[start]==nums[mid] and nums[mid]==nums[end]:     # This handles the cases of repetion
                start+=1
                end-=1
                continue
            if nums[start]<=nums[mid] :   # if left half is sorted
                if nums[start]<=target<=nums[mid]:  # if target is in left sorted half
                    end=mid-1
                else:
                    start=mid+1
            elif nums[end]>=nums[mid]:     # if right half is sorted
                if nums[mid]<=target<=nums[end]:    # if target is in right sorted half
                    start=mid+1
                else:
                    end=mid-1
        return False
