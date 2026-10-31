class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = float('inf')
        maxProfit = 0
        for price in prices:
            maxProfit = max(price - minsofar, maxProfit)
            minsofar = min(price, minsofar)
        return maxProfit
        