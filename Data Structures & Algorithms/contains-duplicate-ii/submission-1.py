class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            cur = nums[R]
            while R - L > k:
                old = nums[L]
                window.remove(old)
                L += 1
            if cur in window:
                return True
            window.add(cur)
            
        return False
            
        