def shiphelp(mid,weights,days): 
    pairs=1
    sum=0
    for i in weights:
        sum+=i
        if sum>mid:
            sum=i
            pairs+=1
    return pairs <= days

class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        answer=0
        left=max(weights)
        right=sum(weights)
        while left<=right:
            mid=(left+right)//2
            if shiphelp(mid, weights, days):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
