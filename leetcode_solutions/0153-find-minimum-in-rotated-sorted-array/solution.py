class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start,end=0,len(nums)-1
        minimum=10000       # since max is 5000

        while start<=end:
            mid=(start+end)//2
            print(start,mid,end)
            print(nums[start:end+1])


            if nums[start]<=nums[mid]:      #That means if left half is rotated
                if minimum>nums[start]:
                    print(minimum, nums[start], "hello")
                    minimum=nums[start]
                start=mid+1
            elif nums[mid]<=nums[end]:  # if right half is rotated
                if minimum>nums[mid]:
                    minimum = nums[mid]
                end=mid-1

        return minimum
