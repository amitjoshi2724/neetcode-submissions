class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        res = 1
        prevSign = 0
        count = 0
        for i in range(1, len(arr)):
            prev = arr[i-1]
            cur = arr[i]
            if cur == prev:
                count = 0
                prevSign = 0
            elif cur > prev and prevSign != 1:
                count += 1
                res = max(count+1, res)
                prevSign = 1
            elif cur < prev and prevSign != -1:
                count += 1
                res = max(count+1, res)
                prevSign = -1
            else:
                count = 1
                prevSign = 1 if cur > prev else -1
        return res
        