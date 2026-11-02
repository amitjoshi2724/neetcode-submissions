class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        resMax = max(nums)
        resMin = min(nums)

        total = 0
        curSumMax = 0
        curSumMin = 0
        for num in nums:
            total += num
            curSumMax = max(num, curSumMax + num)
            curSumMin = min(num, curSumMin + num)
            resMax = max(resMax, curSumMax)
            resMin = min(resMin, curSumMin)
        #print (resMax, resMin)
        if resMax < 0:
            return max(nums)
        return max(resMax, total - resMin)
            
        