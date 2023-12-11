def check(mid,bloomDay,m,k):
    counter=0
    pairs=0
    for i in bloomDay:
        if mid>=i:
            counter+=1
        else:
            counter=0
        if counter==k:
            pairs+=1
            counter=0
    if pairs>=m:
        return True
    else:
        return False
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        length=len(bloomDay)
        answer=-1
        if length>=m*k:
            left=min(bloomDay)
            right=max(bloomDay)
            while left<=right:
                mid=(left+right)//2
                if check(mid,bloomDay,m,k):
                    answer=mid
                    right=mid-1
                else:
                    left=mid+1
        return answer

