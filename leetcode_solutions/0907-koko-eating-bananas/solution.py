class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        maxspeed=max(piles)
        start=1
        end=maxspeed
        while start<=end:
            mid=(start+end)//2
            total_time = 0
            for i in piles:
                time_taken=i//mid
                if i%mid!=0:
                    time_taken+=1
                total_time+=time_taken
            if total_time<=h:
                end=mid-1
            else:
                start=mid+1
        return start
