from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        tdict = defaultdict(lambda: 0)
        for ch in t:
            tdict[ch] += 1
        incomplete = set(tdict.keys())
        
        window = defaultdict(lambda: 0)
        minL,minR = -1,-1
        found = False
        l,r = 0,0
        while r < len(s):
            cur = s[r]
            window[cur] += 1
            if window[cur] == tdict[cur]:
                incomplete.discard(cur)

            while len(incomplete) == 0 and l <= r:
                if found is False or (r-l+1) < (minR - minL + 1):
                    minL, minR = l,r
                    found = True

                prev = s[l]
                window[prev] -= 1
                if window[prev] < tdict[prev]:
                    incomplete.add(prev)
                l += 1
  
            r += 1
        
        if found:
            return s[minL:minR+1]
        else:
            return ""





        