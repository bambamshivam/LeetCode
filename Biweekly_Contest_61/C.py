class Solution:
    def maxTaxiEarnings(self, n: int, l) -> int:
        for i in range(len(l)):
            l[i][2]+=l[i][1]-l[i][0]
        l.sort(key=lambda x:x[1])
        def solve(ar,i):
            l=0
            r=i-1
            while l<=r:
                m=(l+r)//2
                if ar[m][1]<=ar[i][0]:
                    if ar[m+1][1]<=ar[i][0]:
                        l=m+1
                    else:
                        return m
                else:
                    r=m-1
            return -1
        dp=[0 for i in range(len(l))]
        dp[0]=l[0][-1]
        for i in range(1,len(l)):
            cur=l[i][-1]
            t=solve(l,i)
            if t!=-1:
                cur+=dp[t]
            dp[i]=max(cur,dp[i-1])
        return dp[-1]