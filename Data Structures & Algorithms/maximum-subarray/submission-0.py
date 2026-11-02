class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = max(nums)
        curSum = 0
        for num in nums:
            curSum = max(num, curSum + num)
            maxSum = max(curSum, maxSum)
        return maxSum
        