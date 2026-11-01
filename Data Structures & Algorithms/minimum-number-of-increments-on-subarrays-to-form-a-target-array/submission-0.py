class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        prev = 0
        for item in target:
            res += max(0, item - prev)
            prev = item
        return res

        