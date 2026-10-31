class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in d:
                return [d[complement], i]
            d[num] = i
