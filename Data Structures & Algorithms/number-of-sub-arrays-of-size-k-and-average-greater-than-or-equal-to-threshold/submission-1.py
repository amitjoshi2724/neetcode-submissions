class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        res = 0
        windowTotal = 0
        sumThreshold = threshold * k
        for R in range(len(arr)):
            num = arr[R]
            windowTotal += num
            if R - L + 1 > k:
                windowTotal -= arr[L]
                L += 1
            if windowTotal >= sumThreshold and R - L + 1 == k:
                res += 1
                # print (L,R, windowTotal)
        return res

        