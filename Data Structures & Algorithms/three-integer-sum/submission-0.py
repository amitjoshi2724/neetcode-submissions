from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # similar to 2-sum except you look for the complements of pairwise sums rather than individual elems
        nums.sort()

        elems = defaultdict(lambda: 0)
        for num in nums:
            elems[num] += 1

        print (nums)

        res = list()

        for i in range(len(nums)):
            elems[nums[i]] -= 1
            if i != 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                elems[nums[j]] -= 1
                if j != i+1 and nums[j] == nums[j-1]:
                    continue
                cursum = nums[i] + nums[j]
                complement = -1 * cursum
                if complement in elems and elems[complement] > 0:
                    res.append([nums[i], nums[j], complement])
            for j in range(i+1, len(nums)):
                elems[nums[j]] += 1
        return res

        