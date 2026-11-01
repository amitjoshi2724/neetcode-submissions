class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def lcshelper(text1: str, text2: str, i, j) -> int:
            if (i,j) in cache:
                return cache[(i,j)]
            if i == len(text1) or j == len(text2):
                cache[(i,j)] = 0
            else:
                if text1[i] == text2[j]:
                    cache[(i,j)] = 1 + lcshelper(text1, text2, i + 1, j + 1)
                else:
                    cache[(i,j)] = max(lcshelper(text1, text2, i, j+1), lcshelper(text1, text2, i+1, j))

            return cache[(i,j)]

        
        return lcshelper(text1, text2, 0,0)

        