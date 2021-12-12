class Solution(object):
    def maxTotalFruits(self, fruits, s, k):
        m=200000
        pos=[0]*(m+1)
        for i in fruits:
            pos[i[0]]=i[1]
        dp=[0]*(m+1);dp[s]=pos[s]
        for i in range(s+1,m+1):
            dp[i]=dp[i-1]+pos[i]
        for i in range(s-1,-1,-1):
            dp[i]=dp[i+1]+pos[i]
        ma=0
        for i in range(max(0,s-k),s+1):
            t=dp[i]-dp[s]
            p=max(k-(2*(s-i)),0)
            g=dp[min(s+p,m)]-dp[s]
            ma=max(ma,t+g+dp[s])
        for i in range(min(m,s+k),s-1,-1):
            t=dp[i]-dp[s]
            p=max(k-(2*(i-s)),0)
            g=dp[max(s-p,0)]-dp[s]
            ma=max(ma,t+g+dp[s])
        return ma
        