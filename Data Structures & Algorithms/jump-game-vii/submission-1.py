class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False]*len(s)

        for i in range(len(s)-1, -1, -1):
            if i==len(s)-1 and s[i]=="0":
                dp[i]=True
            if dp[i]==True:
                for j in range(i-maxJump, i-minJump+1):
                    if j>=0 and s[j]=="0":
                        dp[j] = True
        #print(dp)
        return dp[0]
