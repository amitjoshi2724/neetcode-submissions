class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n,m = len(str1), len(str2)

        belowRow = [str2[j:] for j in range(m+1)]
        for i in range(n-1,-1,-1):
            #print (belowRow)
            cur = ["" for i in range(m+1)]
            cur[-1] = str1[i:]
            for j in range(m-1,-1,-1):
                if str1[i] == str2[j]:
                    cur[j] = str1[i] + belowRow[j+1]
                else:
                    res1 = str1[i] + belowRow[j]
                    res2 = str2[j] + cur[j+1]
                    if len(res1) <= len(res2):
                        cur[j] = res1
                    else:
                        cur[j] = res2

            belowRow = cur
        print (belowRow[0])
        return belowRow[0]
        
        


        