def helper(nums,mid,threshold):
    sum=0
    for i in nums:
        k=i//mid
        if i%mid!=0:
            k+=1
        sum+=k
        if sum>threshold:
            return False
    if sum<=threshold:
        return True

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        length=len(nums)
        answer=0
        left=1
        right=max(nums)
        while left<=right:
            mid=(left+right)//2
            if helper(nums,mid,threshold):
                answer=mid
                right=mid-1
            else:
                left=mid+1
        return answer
        
