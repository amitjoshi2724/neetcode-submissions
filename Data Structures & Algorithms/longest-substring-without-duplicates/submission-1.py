class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLen = -1
        if s == "":
            return 0
        L = 0
        window = set()
        for R in range(n):
            ch = s[R]
            while ch in window:
                window.remove(s[L])
                L += 1

            curLen = R - L + 1
            maxLen = max(maxLen, curLen)
            window.add(ch)
        return maxLen
            


        