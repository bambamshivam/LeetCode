class Solution:
    def maxConsecutiveAnswers(self, l: str, k: int) -> int:
        n=len(l)
        def solve(c):
            dp=[0]*(n+1)
            m=0
            for i in range(1,n+1):
                dp[i]=dp[i-1]+(l[i-1]==c)
            for i in range(1,n+1):
                t=dp[i-1]
                j=bisect_right(dp,k+t)
                m=max(m,j-i)
            return m
        return max(solve('T'),solve('F'))
        
            