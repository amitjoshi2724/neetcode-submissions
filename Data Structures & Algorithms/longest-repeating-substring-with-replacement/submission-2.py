from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest window with at most k non-majority elems
        def getNonmajority(d, L, R):
            totalElems = R - L + 1
            majorityElems = max(d.values())
            nonmajorityElems = totalElems - majorityElems
            return nonmajorityElems


        d = defaultdict(lambda: 0)
        L = 0
        res = -1
        for R in range(len(s)):
            ch = s[R]
            d[ch] += 1
            #print (L,R, d, getNonmajority(d, L,R))
            while getNonmajority(d, L, R) > k:
                d[s[L]] -= 1
                L += 1
            
            res = max(res, R - L + 1)
            

        return res




        
        