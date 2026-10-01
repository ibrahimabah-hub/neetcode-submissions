class Solution:
    def countSubstrings(self, s: str) -> int:
        numPals = 0
        isPal = [[False]*len(s) for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s), 1):
                if s[i]==s[j] and (j-i<2 or isPal[i+1][j-1]):
                    isPal[i][j] = True
                    numPals +=1

        return numPals