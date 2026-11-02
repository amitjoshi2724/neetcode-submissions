class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float('inf')
        L = 0
        cursum = 0
        for R in range(len(nums)):
            cursum += nums[R]
            while cursum >= target:
                minLen = min(minLen, R - L + 1)
                cursum -= nums[L]
                L += 1
                


        if minLen == float('inf'):
            return 0
        else:
            return minLen