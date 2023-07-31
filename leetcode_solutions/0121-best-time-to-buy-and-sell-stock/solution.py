class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy,sell=0,1    #pointers
        maxprofit=0
        length=len(prices)
        while sell<length:
            if prices[sell]-prices[buy]>maxprofit:
                maxprofit=prices[sell]-prices[buy]
            if prices[sell]<prices[buy]:
                buy=sell
            sell+=1
        return maxprofit
           
